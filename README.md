## DEVELOPMENT zaptec charger custom component for home assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]][license]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]


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

In some cases it would help debugging to have access to the diagnostics info.
Please see the "Diagnostics" section below in how to generate if it is requested.


## Installation

This repo can be installed manually into Home Assistant by manually adding the
URL in HACS.

**:information_source: NOTE!** Existing `zaptec` installations MUST be
uninstalled first. Installing this repo will clash with existing integration
already installed.

### Step 1
![Setup1](/img/hacs_custom.png)

### Step 2
![Setup2](/img/hacs_zaptec_custom.png)

### Step 3
![Setup3](/img/hacs_zaptec_dev.png)


## What's new

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


### Zaptec device concept

Zaptec use three levels of abstractions in their EVCP setup.

* Installation - This is the top-level entity and represents the entire site.
* Circuit - An installation can have one or more (electrical) circuits. One circuit
  have one common circuit breaker.
* Charger - This is the actual EV charge point connected to a circuit. Each
  circuit might have more than one charger.


## How to use it

### Start & stop charging

Starting and stopping charging can be done by several methods. If the charger
is configured to no require authentication, connecting the charger to the
EV will by default start charging.

To start the charging from HA, this can be done in several ways:

- Press the "Resume charging" button, or
- Toggle the "Charging" switch, or
- Send `zaptec.restart_charger` service call

Similarly, pausing the charging can be done by:

- Pressing the "Stop/pause charging" button, or
- Toggle the "Charging" switch (if it was active), or
- Send `zaptec.stop_pause_charging` service call

**:information_source: NOTE:** Zaptec will unlocks the cable when charging
is paused unless it is permanently locked.


### Setting charging current

The "Available current" number entity in the installation device will set
the maximum current the EV can use. This slider will set all 3 phases at
the same time.

**:information_source: NOTE!** This entity is adjusting the available current for the
entire installation. If the installation has several chargers installed,
changing this value will affect all.

The "Available current" number can be used to prevent the charger from
automatically start charging by setting the value to 0. To start charging
a non-zero value must be set.

**:information_source: NOTE!** Many EVs doesn't like getting too frequent changes
to the available charge current. Zaptec recommends not changing the values
more often than 15 minutes.

#### 3 phase current adjustment

The service call `limit_current` can be used with the arguments `available_current_phase1`, `..phase2` and `..phase3` to set the available
current on individual phases.


### Require charging authorization

Many users wants to setup their charger to require authorization before giving
power to charge any EV. This integration does not offer any options to configure
authorization, please use the official [Zaptec portal](https://portal.zaptec.com/)
or app to configure and set up.

When an EV charging cable is inserted into the charger, it will go into _Waiting_
mode until it has been authorized. This can be done with RFID tags, the Zaptec
app and more.

If the installation is configured for _native authentication_ it is possible
to authorize charging from Home Assistant using the "Authorize charging"
button. It stays authorized until either the cable is removed or the button
"Deauthorize charging" is pressed.

**:information_source: INFO:** Please note that Zaptec unlocks the cable when charging
is paused unless it is permanently locked.


### Diagnostics

The integration supports downloading of diagnostics data. This can be reached
by `Settings -> Devices & Services -> <one of your zaptec devices>` and then
press the "Download diagnostics". The file downloaded is anonymized and should
not contain any personal information. Please double check that the file
doesn't contain any personal information before sharing.


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
