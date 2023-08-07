# pylint: disable=C0116

import asyncio
import logging
from datetime import timedelta

import aiohttp
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import STATE_UNAVAILABLE

# from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.dispatcher import (
    async_dispatcher_connect,
    async_dispatcher_send,
)
from homeassistant.helpers.typing import ConfigType, HomeAssistantType

from .const import *

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(seconds=60)


async def _dry_setup(hass, config, async_add_entities, discovery_info=None):
    sensors = []
    acc = hass.data[DOMAIN]["api"]
    use_uid = config.get("use_uid", True)  # FIXME: How to deal with old behavior?

    async def callback(data):
        """Callback thats executed when a new message from the message bus is in."""
        acc.update(data)
        # Tell the sensor that there is an update.
        async_dispatcher_send(hass, EVENT_NEW_DATA)

    # Not sure this should be added, lets see
    hass.data[DOMAIN]["producer"].append(callback)

    for ins in acc.installs:
        await ins.stream(cb=callback)
        for circuit in ins.circuits:
            # _LOGGER.debug("Building circuit %s", circuit)
            c = CircuitSensor(circuit, hass, use_uid=use_uid)
            sensors.append(c)
            for charger in circuit.chargers:
                _LOGGER.debug("Building charger %s", charger.id)
                # Force a update before its added.
                await charger.state()
                chs = ChargerSensor(charger, hass, use_uid=use_uid)
                sensors.append(chs)
        sensors.append(InstallationSensor(ins, hass, use_uid=use_uid))

    for charger in acc.stand_alone_chargers:
        _LOGGER.debug("charger %s", charger.id)
        if charger.id in acc.map:
            _LOGGER.debug(
                "Skipping standalone charger %s as its already exists.", charger.id
            )
            continue
        else:
            # _LOGGER.debug("Building charger %s", charger)
            # Force an update before its added.
            await charger.state()
            chs = ChargerSensor(charger, hass, use_uid=use_uid)
            sensors.append(chs)

    async_add_entities(sensors, False)

    return True


async def async_setup_platform(
    hass: HomeAssistantType, config: ConfigType, async_add_entities, discovery_info=None
) -> None:  # pylint: disable=W0613
    return True


async def async_setup_entry(hass, config_entry, async_add_devices):
    return await _dry_setup(hass, config_entry.data, async_add_devices)


class ZapMixin:
    _attr_device_info = None
    _attr_unique_id = None
    _attr_has_entity_name = True
    _attr_name = None
    _attr_native_value = None

    async def _real_update(self):
        _LOGGER.debug("Called _real_update for %s", self.__class__.__name__)
        # The api already updated and have new data available.
        self.async_write_ha_state()

    async def async_added_to_hass(self):
        """Connect to dispatcher listening for entity data notifications."""
        await super().async_added_to_hass()
        _LOGGER.debug("called async_added_to_hass %s", self.__class__.__name__)
        self.async_on_remove(
            async_dispatcher_connect(self._hass, EVENT_NEW_DATA, self._real_update)
        )

    @property
    def should_pull(self):
        return False


class CircuitSensor(ZapMixin, SensorEntity):
    def __init__(self, circuit, hass, use_uid=False):
        self._api = circuit
        self._attrs = circuit._attrs
        self._hass = hass
        self._use_uid = use_uid

    @property
    def name(self) -> str:
        if self._use_uid:
            ids = self._attrs["id"]
            return "Zaptec Circuit %s" % ids
        ids = self._attrs["name"]
        return "%s Circuit" % ids

    @property
    def icon(self) -> str:
        return "mdi:orbit"

    @property
    def extra_state_attributes(self) -> dict:
        return self._attrs

    @property
    def unique_id(self):
        return f"zaptec_{self._attrs['id']}".lower()

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self.name,
            "manufacturer": DOMAIN,
        }

    @property
    def state(self):
        return self._attrs["active"]


class InstallationSensor(ZapMixin, SensorEntity):
    def __init__(self, api, hass, use_uid=False):
        self._api = api
        self._attrs = api._attrs
        self._hass = hass
        self._use_uid = use_uid

    @property
    def name(self) -> str:
        if self._use_uid:
            ids = self._attrs["id"]
            return "Zaptec Installation %s" % ids
        ids = self._attrs["name"]
        return "%s Installation" % ids

    @property
    def icon(self) -> str:
        return "mdi:home-lightning-bolt-outline"

    @property
    def extra_state_attributes(self) -> dict:
        return self._attrs

    @property
    def unique_id(self):
        return f"zaptec_{self._attrs['id']}".lower()

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self.name,
            "manufacturer": DOMAIN,
        }

    @property
    def state(self):
        return self._attrs["active"]


class ChargerSensor(ZapMixin, SensorEntity):
    def __init__(self, api, hass, use_uid=False) -> None:
        self._api = api
        self._hass = hass
        self._attrs = api._attrs
        self._state = STATE_UNAVAILABLE
        self._use_uid = use_uid

    @property
    def name(self) -> str:
        if self._use_uid:
            ids = self._api.mid.lower()
            return "Zaptec Charger %s" % ids
        else:
            ids = self._attrs["name"]
            return str(ids)

    @property
    def icon(self) -> str:
        return "mdi:ev-station"

    @property
    def entity_picture(self) -> str:
        return CHARGE_MODE_MAP[self._attrs["operating_mode"]][1]

    @property
    def unique_id(self):
        return f"{DOMAIN}_{self._attrs['id']}_chargers".lower()

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self.name,
            "manufacturer": DOMAIN,
        }

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self) -> dict:
        return self._attrs

    async def _real_update(self):
        _LOGGER.debug("Called _real_update for %s", self.__class__.__name__)
        # The api already updated and have new data available.
        try:
            value = CHARGE_MODE_MAP[self._attrs["operating_mode"]][0]
            self._state = value
        except KeyError:
            # This seems to happen when it starts up.
            self._state = STATE_UNAVAILABLE

        self.async_write_ha_state()
