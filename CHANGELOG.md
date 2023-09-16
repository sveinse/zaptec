# Changelog

## 0.0.6b230916

* Fix better error handling if the zaptec login provides less access, such as
  ordinary users without any privilege status. It crashed the configuration
  and prevented any use of the component. sveinse/github#10
* Ensure entities are marked as "Unavailable" if they don't exists in Zaptec
  and ensure the startup doesn't fail without them
* Fix text for binary sensor "charger.is_authorization_requried"
* Fix more user friendly error messages

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
