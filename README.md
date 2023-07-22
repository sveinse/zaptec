## zaptec charger custom component for home assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

### Usage
Use hacs to install the package, add the config example for more usage see the `lovelace_example`

Setup the integration using the integrations page.


### Zaptec concept

Zaptec use three levels of abstractions in their EVCP setup.

* Installation - This is the top-level entity and represents the entire site.
* Circuit - An installation can have one or more (electrical) circuits. One circuit
  have one common circuit breaker.
* Charger - This is the actual EV charge point connected to a circuit. Each
  circuit might have more than one charger.


### Pause and resuming charging

Pausing charging can be set by issuing the service `zaptec.stop_pause_charging`

```yaml
- service: zaptec.stop_pause_charging
  data:
    charger_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

The charger ID can be read from the `ID` attrbute under the `zaptec_charger_*`
entity.

Resuming charging is done the same way:

```yaml
- service: zaptec.resume_charging
  data:
    charger_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### Set charge current

The charge current can be set by issuing the service `zaptec.limit_current`.
It sets the maximum current available on the _installation_ and will affect all
circuits and chargers.

```yaml
- service: zaptec.limit_current
  data:
    installation_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    available_current: 12
```

The installation ID can be found as the `ID` attribute under the
entity named `zaptec_installation_*`.

Please note that the Zaptec API docs warns against settings the current too
frequest as charging cars might trigger an error if it changes too often. Once
per 15 minutes is recommended.


### Disable auto charge start

Zaptec seems to start charging automatically when a charge ready EV is
connected to a charger. This might not be wanted behavior if delayed start is
wanted. The following trick will put the charger in _waiting_ mode and not
start immediately:

1. Set the available current to 0 (which must be done before the EV is
   plugged in)
2. Connect the EV
3. When ready to charge, set the available current to the wanted value

If the available current is set back to 0, the Zaptec will put the charge
session into _finished_ mode. Thus setting of the available current is an
effective way to start and stop the charging.

Note that the avaialable acts on the entire installation. If you have multiple
circuits and/or chargers, this will apply to all of them!


[zaptec]: https://github.com/custom-components/zaptec
[buymecoffee]: https://www.buymeacoffee.com/hellowlol1
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/custom-components/zaptec.svg?style=for-the-badge
[commits]: https://github.com/custom-components/zaptec/commits/master
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Default-blue.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license]: https://github.com/custom-components/zaptec/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/custom-components/zaptec.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Hellowlol-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/zaptec.svg?style=for-the-badge
[releases]: https://github.com/custom-components/zaptec/releases
[user_profile]: https://github.com/hellowlol
