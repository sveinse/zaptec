"""Zaptec integration constants."""
from __future__ import annotations

NAME = "zaptec-dev"
VERSION = "0.0.6b230807"
ISSUEURL = "https://github.com/sveinse/zaptec/issues"

STARTUP = """
-------------------------------------------------------------------
{name}
Version: {version}
This is a custom component
If you have any issues with this you need to open an issue here:
{issueurl}
-------------------------------------------------------------------
""".format(
    name=NAME, version=VERSION, issueurl=ISSUEURL
)

DOMAIN = "zaptec"
OBSERVATIONS_REMAPS = {}
WANTED_ATTRIBUTES = []
CHARGE_MODE_MAP = {
    "Unknown": ["Unknown", "mdi:help-rhombus-outline"],
    "Disconnected": ["Disconnected", "mdi:power-plug-off"],
    "Connected_Requesting": ["Waiting", "mdi:timer-sand"],
    "Connected_Charging": ["Charging", "mdi:lightning-bolt"],
    "Connected_Finished": ["Charge done", "mdi:battery-charging-100"],
}

TOKEN_URL = "https://api.zaptec.com/oauth/token"
API_URL = "https://api.zaptec.com/api/"
CONST_URL = "https://api.zaptec.com/api/constants"

CONF_SENSOR = "sensor"
CONF_SWITCH = "switch"
CONF_ENABLED = "enabled"
CONF_NAME = "name"

EVENT_NEW_DATA = "event_new_data_zaptec"
EVENT_NEW_DATA_HOURLY = "event_new_data_hourly_zaptec"

DEFAULT_SCAN_INTERVAL = 60

MANUFACTURER = "Zaptec"

REQUEST_REFRESH_DELAY = 0.3

class Missing:
    '''Singleton class representing a missing value.'''
MISSING = Missing()

TRUTHY = ["true", "1", "on", "yes", 1, True]
FALSY = ["false", "0", "off", "no", 0, False]
