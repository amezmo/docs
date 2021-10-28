

# Restart a Worker

`POST` /v1/instances/{instance_id}/workers/{worker_id}/restart

## Parameters
Parameter     |  Type | In     | Description     
--------------|------|---------|------------------
instance_id   |  string | uri  | The instance ID
worker_id     | string | uri   | The woker ID



## Code samples

```bash
curl --request POST \
    --url https://api.amezmo.com/v1/instances/{instance_id}/workers/{worker_id}/restart \
    --header 'Authorization: Bearer {api_key}'
```

## Response

`200 OK`

```bash
{
    "id": 838,
    "status": "Restarting",
    "name": "Laravel queue",
    "command": "php artisan queue:work --sleep=3 --tries=3 -vvv",
    "stop_wait_seconds": 10,
    "auto_restart": 1,
    "start_retries": 3,
    "worker_processes": 1,
    "created_at": "2021-06-27 03:32:48",
    "log_file_path": "\/backups\/logs\/1adb3c27-9a23-48c3-83f1-05ec9754c479-worker.log"
}
```
