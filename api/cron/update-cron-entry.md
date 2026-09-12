# Update a cron entry

{.lead}
Update the **script** a cron entry runs, its **schedule**, or both, without
recreating the entry.

`PATCH` /v1/instances/{instance_id}/cron/{cron_id}

## Parameters

Parameter   | Type   | In   | Required    | Description
----------- | ------ | ---- | ----------- | -------------------------------------------------------
instance_id | string | uri  | Yes         | The instance ID
cron_id     | string | uri  | Yes         | The cron entry ID. See [List cron entries](list-cron-entries.md)
command     | string | body | Conditional | The bash script to run. Required when you omit `expression`
expression  | string | body | Conditional | The schedule. Required when you omit `command`

Send `command`, `expression`, or both. A field you leave out keeps its current
value, and a request that carries neither returns a validation error.

Use `--data-urlencode` rather than `--data` for both fields. A script contains
newlines and an expression contains spaces and `*`, and only the encoding form
sends those intact.

Read the current values first with
[Get a cron entry](get-cron-entry.md), so a partial update starts from what is
actually on the instance.

`expression` accepts a five-field POSIX cron expression or one of the aliases
below. Not every expression the API accepts runs on a Linux instance: see
[custom cron expressions](../../cron/custom-expressions.md) for the extensions to
avoid.

Alias              | Expression    | Runs
------------------ | ------------- | -------------------------
`@minutely`        | `* * * * *`   | Every minute
`@every_5_minutes` | `*/5 * * * *` | Every five minutes
`@hourly`          | `0 * * * *`   | At the top of every hour
`@daily`           | `0 0 * * *`   | Every day at midnight
`@weekly`          | `0 0 * * 0`   | Every Sunday at midnight
`@monthly`         | `0 0 1 * *`   | On the first of every month
`@yearly`          | `0 0 1 1 *`   | On January 1
`@annually`        | `0 0 1 1 *`   | On January 1

The response reports the resolved five-field `expression` along with the
matching `expression_alias`, so an alias you send back comes out as both.

> [!NOTE]
> A cron entry's `name` is fixed. Amezmo derives the entry's log file name from
> it, so renaming would leave the existing log behind under the old name. To
> change a name, delete the entry from the dashboard and
> [create a new one](create-cron-entry.md).
> [Editing a cron entry](../../cron/editing-entries.md) covers the same
> limitations for the dashboard form.

Amezmo applies the change on your instance asynchronously: it rewrites the
script and the crontab entry in place, so the entry keeps its ID and its log
file. A run already in flight finishes under the old script.

Updating an entry that is being deleted returns `409 Conflict` with the code
`cron_entry_deleting`. An instance whose type does not include cron returns
`422` with `feature_not_supported`. See [Errors](../errors.md) for the shape of
both.

## Code samples

### Request example

{title="PATCH /v1/instances/{instance_id}/cron/{cron_id}"}
```bash
curl https://api.amezmo.com/v1/instances/{instance_id}/cron/412 \
    -X PATCH \
    -H "Authorization: Bearer $AMEZMO_API_KEY" \
    --data-urlencode command="#!/bin/bash
php artisan schedule:run --no-interaction
" \
    --data-urlencode expression='@every_5_minutes'
```

### Response

{title="200 OK"}
```javascript
{
    "id": 412,
    "name": "Laravel-task-scheduler",
    "command": "#!/bin/bash\nphp artisan schedule:run --no-interaction",
    "expression": "*/5 * * * *",
    "expression_alias": "@every_5_minutes",
    "status": "Created",
    "environment_name": "production",
    "log_file_path": "/home/deployer/cron/logs/cron.Laravel-task-scheduler.log",
    "created_at": "2026-02-11T18:04:22.000000Z",
    "updated_at": "2026-09-10T14:31:07.000000Z"
}
```
