# Changelog

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
