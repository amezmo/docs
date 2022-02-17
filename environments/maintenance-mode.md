# Maintenance Mode

Maintenance Mode disables access to your application by returning a maintenance page to your visitors. During the time
when Maintenance Mode is enabled, your app responds with a static page indicating that your app is down for maintenance.

While in Maintenance Mode, the HTTP status code 503 is returned to your visitors. During this time, your [Workers](/docs/workers) will
not be paused, and any [Cron](/docs/cron) jobs will also not be paused.
Maintenance Mode effects inbound HTTP requests to your application only.

MySQL is placed in read-only mode during the time your application is in Maintenance Mode. 

While Maintenance Mode prevents your application from responding to HTTP requests, the instance is still active. To shut down the instance completely, see the section on [pausing instances](/docs/instances/pausing). 