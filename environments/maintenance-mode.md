# Maintenance Mode

Maintenance Mode disables access to your application by returning a maintenance page to your visitors. During the time
when Maintenance Mode is enabled, your app responds with a static page indicating that your app is down for maintenance.

While in Maintenance Mode, the HTTP code 503 is returned to your visitors. During this time, your workers will
not be paused, and any Cron jobs will also not be paused.
Maintenance Mode effects inbound HTTP requests to your application only.
