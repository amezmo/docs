# Create a cron entry

{.lead}
Create a **cron entry** on an instance: a name, a bash script, and the
schedule to run it on.

`POST` /v1/instances/{instance_id}/cron

## Parameters

Parameter   | Type   | In   | Required | Description
----------- | ------ | ---- | -------- | -------------------------------------------------------
instance_id | string | uri  | Yes      | The instance ID
name        | string | body | Yes      | A permanent name for the entry, unique in its environment
command     | string | body | Yes      | The bash script to run
expression  | string | body | Yes      | The schedule
environment | string | body | Yes      | The environment the entry runs in: `production` or `staging`

`name` accepts letters, numbers, and hyphens, starts with a letter or a
number, and is at most 63 characters. Pick it carefully: Amezmo derives the
entry's log file name from it, so the name is fixed after creation.
[Update a cron entry](update-cron-entry.md) updates the script and the
schedule, never the name.

Use `--data-urlencode` rather than `--data` for both `command` and
`expression`. A script contains newlines and an expression contains spaces and
`*`, and only the encoding form sends those intact.

`expression` accepts a five-field POSIX cron expression or one of the aliases
below. Not every expression the API accepts runs on a Linux instance: see
[custom cron expressions](../../cron/custom-expressions.md) for the extensions
to avoid.

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
matching `expression_alias`, so an alias you send comes out as both.

Amezmo applies the entry on your instance asynchronously: it writes the script
and the crontab entry, and runs begin at the next time the schedule matches.
The response carries the entry immediately, including the `id` you use with
[Get a cron entry](get-cron-entry.md) and
[Update a cron entry](update-cron-entry.md).

A name already taken in the same environment returns `409 Conflict` with the
code `cron_entry_exists`. An environment your instance does not have returns
`422` with `business_logic_error`. An instance whose type does not include
cron returns `422` with `feature_not_supported`. See [Errors](../errors.md)
for the shape of all three.

Delete a cron entry from the dashboard, under **Cron** on your instance.

## Code samples

### Request example

{title="POST /v1/instances/{instance_id}/cron"}
```bash
curl https://api.amezmo.com/v1/instances/{instance_id}/cron \
    -X POST \
    -H "Authorization: Bearer $AMEZMO_API_KEY" \
    --data-urlencode name='Laravel-task-scheduler' \
    --data-urlencode command="#!/bin/bash
php artisan schedule:run
" \
    --data-urlencode expression='@minutely' \
    --data-urlencode environment='production'
```

### Response

{title="201 Created"}
```javascript
{
    "id": 412,
    "name": "Laravel-task-scheduler",
    "command": "#!/bin/bash\nphp artisan schedule:run",
    "expression": "* * * * *",
    "expression_alias": "@minutely",
    "status": "Created",
    "environment_name": "production",
    "log_file_path": "/home/deployer/cron/logs/cron.Laravel-task-scheduler.log",
    "created_at": "2026-02-11T18:04:22.000000Z",
    "updated_at": "2026-02-11T18:04:22.000000Z"
}
```
