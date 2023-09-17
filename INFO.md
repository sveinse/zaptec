## DEVELOPMENT zaptec charger custom component for home assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]


# Features

* Integration for Home assistant for Zaptec Chargers through the Zaptec
  cloud API
* Provides start & stop of charging the EV
* Supports basic (native authentication)
* Sensors and status, current, energy
* Adjustable charging currents

To use this component, a user with access to
[Zaptec Portal](https://portal.zaptec.com/) is needed.

Confirmed to work with

* Zaptec Go

> *) Send a message to @sveinse if you have been able to use any other chargers
in order to put it on the list.


## :warning: Development version

**:information_source: IMPORTANT!** This is https://github.com/sveinse/zaptec
which is @sveinse fork of upstream/official zaptec integration at
https://github.com/custom-components/zaptec.
This is under active development, and any feedback on your experience using it
is very appreciated.

**:warning:  WARNING!** This is a major refactor of the upstream zaptec
integration. The names and device setup has been significantly refactored.
Installing this version will break your existing automations and templates.


## Beta testing

The component is currently under beta testing. Any feedback on problems,
improvements or joy can be given at: https://github.com/sveinse/zaptec/issues

In particular the following items is of particular interest:

* Is everything working as it should? Any error messages?
* Does your autpmations and operation of the charger work with your use?
* Any missing entities (sensors, buttons, switches)?
* Are the new entity names ok?
* What is missing from documentation?

In some cases it would help debugging to have access to the diagnostics info.
Please see the "Diagnostics" section below in how to generate if it is requested.


## What's new in this Beta

The zaptec integration has been completely refactored and the way to interact
with it in Home Assistant has changed. The zaptec data is now represented as
proper entities (like sensors, numbers, buttons, etc). This makes logging and
interactions much simpler and it needs no additional templates.

The integration is set up as one devices for each of the detected Zaptec
devices. Most users will have three devices: An installation device, a circuit
and a charger and each provide different functionality.

The previous zaptec entities were named `zaptec_charger_<uuid>`,
`zaptec_installation_<uuid>` and `zaptec_circute_<uuid>`. The full data were
available as attributes in these objects, and they could be retried with
the aid of manual templates. The same objects exists, but under the names
`<name> Installer`, `<name> Charger` and `<name> Circuit`.


[zaptec]: https://github.com/custom-components/zaptec
[buymecoffee]: https://www.buymeacoffee.com/hellowlol1
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/custom-components/zaptec.svg?style=for-the-badge
[commits]: https://github.com/custom-components/zaptec/commits/master
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license]: https://github.com/custom-components/zaptec/blob/main/LICENSE
[license-shield]: https://img.shields.io/github/license/custom-components/zaptec.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Joakim%20Sørensen%20%40ludeeus-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/integration_blueprint.svg?style=for-the-badge
[releases]: https://github.com/custom-components/zaptec/releases
[user_profile]: https://github.com/hellowlol
