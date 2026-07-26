# Post-Deployment Health Checks

After a [successful deployment](directories.md#successful-deployments), Amezmo
can run a health check against an endpoint you choose. Amezmo makes an HTTP
request to that endpoint and checks the response status. Only a 200 passes.
Any other status fails the health check and Amezmo emails you.

The health check runs after a deployment meets the criteria to be considered
successful and after the [release directory](directories.md) is promoted to the
current release.

A [deployment hook](hooks/index.md) can miss a problem that only shows up once
traffic reaches your app. A health check catches those cases, so you hear about
a broken release right away instead of from your users.

## Configuring a Health Check

Configure the health check per environment from the Deployments tab, in the
Settings section:

- Turn the health check on.
- Enter the endpoint URL to request after each deployment.
- Add up to four email addresses to notify when a check fails.

Point the check at a route that exercises your real dependencies, and return a
200 only after your database, Redis and anything else your app needs are
reachable. A route that returns 200 before its dependencies are ready reports a
broken release as healthy.

## Rolling Back a Release

When a health check fails, roll back from the Deployments tab in your dashboard.
Rolling back changes your current release to a previous
[release](releases.md), so your site serves the last version you know worked
while you investigate.
