

# Restart a Worker

`POST` /api/sites/{site_id}/workers/{worker_id}/restart

## Parameters
Parameter     |  Description       
------------- | ------------- 
site_id       | The Site ID
worker_id     | The Worker ID


## Response

`200 OK`

```bash
{
    "id": 838,
    "name": "aaa",
    "command": "php artisan queue:work --sleep=3 --tries=3 -vvv",
    "stop_wait_seconds": 10,
    "auto_restart": 1,
    "start_retries": 3,
    "worker_processes": 1,
    "created_at": "2021-06-27 03:32:48",
    "status": "Restarting",
    "log_file_path": "\/backups\/logs\/1adb3c27-9a23-48c3-83f1-05ec9754c479-worker.log"
}
```
