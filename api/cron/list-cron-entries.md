# List cron entries

{.lead}
List every **cron entry** on an instance, across all of its environments.

`GET` /v1/instances/{instance_id}/cron

## Parameters

Parameter   | Type   | In  | Required | Description
----------- | ------ | --- | -------- | ---------------
instance_id | string | uri | Yes      | The instance ID

Each entry reports the environment it belongs to in `environment_name`, so one
call covers both staging and production. To get a single entry, see
[Get a cron entry](get-cron-entry.md). To update one, see
[Update a cron entry](update-cron-entry.md).

## Code samples

### Request example

{title="GET /v1/instances/{instance_id}/cron"}
```bash
curl https://api.amezmo.com/v1/instances/{instance_id}/cron \
    -H "Authorization: Bearer $AMEZMO_API_KEY"
```

### Response

{title="200 OK"}
```javascript
[
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
        "updated_at": "2026-09-10T14:31:07.000000Z"
    }
]
```
