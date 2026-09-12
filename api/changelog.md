# API changelog

The changelog lists forward-compatible changes to the API.

## 2026-09-12

Added
: [Create a cron entry](cron/create-cron-entry.md) creates an entry on an
instance: a permanent name, a bash script, a schedule, and the environment to
run it in. Deleting an entry stays in the dashboard.

## 2026-09-10

Breaking
: `type` on an error response is now the coarse class of the error
(`invalid_request_error`, `authentication_error`, `rate_limit_error`,
`api_error`) rather than the specific reason. The specific reason moved to the
new `code` field, keeping the strings it used before, so a client matching on
`unknown_resource_error` or `validation_error` should read `code` instead of
`type`. See [Errors](errors.md).

Added
: `code` to every error response: the specific, machine-readable reason, where
`type` is the coarse class. See [Errors](errors.md).

Fixed
: Errors that carry their own response body (no payment method, unverified
email, an instance that is paused or still launching, a feature your instance
type does not include) returned a generic `500` with no usable message. They now
return their real status, message, and `code`.

Fixed
: Error messages written for users were replaced with "An unexpected API error
occurred." outside development. The real message is now returned, and only
genuinely unexpected failures fall back to a generic one.

Added
: [Cron endpoints](cron/index.md). [List cron entries](cron/list-cron-entries.md)
lists every entry on an instance, and
[Get a cron entry](cron/get-cron-entry.md) gets one by ID.
: [Update a cron entry](cron/update-cron-entry.md) updates the `command`, the
`expression`, or both, on an existing entry. An entry's `name` stays fixed,
because Amezmo derives its log file name from it.

## 2022-12-12

Added
: `current_deployment` to [Get Environment](environments/get-environment.md)

## 2022-04-18

Added
: `ssh_enabled` and `trusted_ssh_ips` parameters to [Update Environments](environments/update-environment.md). In addition to accepting these parameters in the PUT
request, they are also shown in the [Get an environment](environments/get-environment.md) resource.

## 2022-01-19

Added
: `newrelic_license_key` parameter to [Update Environments](environments/update-environment.md)

## 2020-10-14

Added
: New optional request properties to [Deployments](deployments/post.md)
