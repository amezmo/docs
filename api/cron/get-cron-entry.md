# Get a cron entry

{.lead}
Get a single **cron entry** by ID, including its schedule and its script.

`GET` /v1/instances/{instance_id}/cron/{cron_id}

## Parameters

Parameter   | Type   | In  | Required | Description
----------- | ------ | --- | -------- | -------------------------------------------------------
instance_id | string | uri | Yes      | The instance ID
cron_id     | string | uri | Yes      | The cron entry ID. See [List cron entries](list-cron-entries.md)

The response carries the entry's full `command`, so this is how you read a
script before updating it with [Update a cron entry](update-cron-entry.md). A
freshly created entry needs no follow-up request: the response of
[Create a cron entry](create-cron-entry.md) carries the same fields.

## Code samples

### Request example

{title="GET /v1/instances/{instance_id}/cron/{cron_id}"}
```bash
curl https://api.amezmo.com/v1/instances/{instance_id}/cron/412 \
    -H "Authorization: Bearer $AMEZMO_API_KEY"
```

### Response

{title="200 OK"}
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
    "updated_at": "2026-09-10T14:31:07.000000Z"
}
```
