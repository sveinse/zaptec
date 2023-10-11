# Changelog

## 0.0.6b231011

* Add TOTAL_INCREASING to "total_charger_power_session", sveinse/zaptec#23
* Fix regression of missing services, sveinse/zaptec#24
* Refactor services in order to make them easier to use with the service call
  UIs 

## 0.0.6b231009

* Rename option "name" to "prefix" to avoid misunderstandings.

Minor house-keeping tasks:
* Minor FIXME cleanups
* Simplify ZaptecUpdateCoordinator init
* Fix logging format for consistency
* Simplify entity setup. Not require account or config entry.
* Renamed ZaptecBaseEntry.create_from() to .create_from_descriptions()

## 0.0.6b231001

* Add support for selecting which chargers to add to zaptec, sveinse/zaptec#5
  by adding a second configuration screen.
* Add support for adding an optional prefix to the device names,
  sveinse/zaptec#4
* Increased API timeout to 60 seconds, sveinse/zaptec#19
* Updated UI messages/translations
* Fixup general error handling

API changes:
* Added RequestConnectionError and RequestDataError, rename AuthorizationError
  to AuthenticationError
* Remove auto state retrieval from build(). When discovering the hierarchy
  there's no need for all the extra information if the object is not going
  to be used. Account.update_states() can be used to update the states for
  all objects in the map.
* Add support for pointing to the object's parent. Add optional installation=
  argument to Charger(). Add optional circuit= argument to Charger().
* Rename Account.installs to Account.installations for consistency
* Add Account.unregister()
* Cleanup error handling for Account.check_login() and add timeout
* Fix error and timeout handling in Account._request(), and fix logging
* Added Account.get_chargers() to get the list of chargers from the map

## 0.0.6b230924

* Fix timeout issue, sveinse/zaptec#19
* Fix sensor state class on "signed_meter_value_kwh" making it possible to use
  in HA energy, sveinse/zaptec#16

## 0.0.6b230918

* Format with black
* Add support of decoding the api attributes that is encoded with OCMF. This
  includes `CompletedSession` and `SignedMeterValue`
* Remove no-nothing method `Charger.update()`
* Improve redaction. Add fields that should be redacted and add a second pass
  to catch text earlier in the output that should be redacted. sveinse/zaptec#7
* Minor cleanups

## 0.0.6b230917

* Fix better error handling if the zaptec login provides less access, such as
  ordinary users without any privilege status. It crashed the configuration
  and prevented any use of the component. sveinse/zaptec#10
* Ensure entities are marked as "Unavailable" if they don't exists in Zaptec
  and ensure the startup doesn't fail without them
* Fix text for binary sensor "charger.is_authorization_requried"
* Added sensor "total_charge_power_session"
* Fixed bug in unity of "total_charge_power"
* Fix non-working authorize and deauthorize commands, sveinse/zaptec#2
* Fix non-working stop charging commands, sveinse/zaptec#15. Possibly zaptec
  have changed their names. Rename to stop_charging_final()
* Fix more user friendly error messages
* Fix bug in error reporting and logging
* Fixed bug in entity unit of Charger.total_charge_power
* Added missing validation tests
* Entity rename for more inituitive names

## 0.0.6b230914

* Added parsing of incoming data from Zaptec API with pydantic. Verify
  critical internally used fields. See validate.py
* Convert "available_current_phaseX" from number to sensor. It's not trivial
  to create a good automatic system for setting via number as all three values
  are needed. If 3 phase adjustment is needed, the service call offes support
  of it.
* Add new sensors "voltage_phase(1|2|3)", "total_charge_power",
  "signed_meter_value", "completed_session_energy", "charger_min/max_current",
  "firmware update", "authorization_required"
* Fix bug in upgrade_firmware button (was update_firmware). Naming was wrong.
* Fix bug in diagnostics that prevented proper hierarchy from being dumped
* Implement ability to get dict items from ZaptecBaseEntity._get_zaptec_value().
  Was needed for "completed_session_energy".

API changes:
* Add ZaptecBase.ATTR_TYPES for converting attributes to specific types
* Rename Installation.set_limit_current()
* Add Installation.set_authentication_required()
* Add Charger.set_current_in_minimum/maximum()
* Remove _req_* methods and add individual functions to retrieve info in each
  class
* Charger commands are now available as named methods or through command()
* Added option for low-level API request logging
* Fixup api build()
* Fix logging

## 0.0.6b230810

* Remove unused globals from const.py
* Cleanup logging
* Introduce ._prev_value, ._log_value(), .key in ZaptecBaseEntity
* Make service definitions into table for easier overview
* Fix missing services.yaml

## 0.0.6b230809

* Add exceptions in API
* Fix exception handling in Account._request
* Limit number of authentication failed retries before giving up

## 0.0.6b230808

User:
* Added buttons "Authorize charging", "Deauthorize Charging"
* Added sensors "Current phase 1,2,3"
* Added service "authorized_charging" and "deauthorize_charging"

Technical:
* Fixed up api.Charger.command() and removed _send_command()
* Added API command "authorizecharge" which was uncovered by @JensDebergh

## 0.0.6b230807

Major refactoring
* Objective: make component more inline with HA coding style
* Use data update coordinator for polling entities
* Data coordinator also handles zaptec stream updates
* Easy to add entities for any (new) Zaptec data points
* Flexible entities in many platforms
* Currently binary sensor, button, number, sensor and switch
* API: Added mc-nbfx decoder for stream messages
* API: Refactored stream handling

User:
* Zaptec devices (installation, circuit and charger) are named as set in Zaptec portal
* More entities for each device. Avoid using attrs and templates.
* Added buttons and number actions as alternatives to services
* Added "Download diagnostics"
