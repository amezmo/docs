
# Get an environment

`GET` /v1/instances/{instance_id}/environments/{name}

## Parameters
Parameter     |  Type | In    | Description     
------------- | ------|------ |------------------
instance_id   |  string | uri  | The instance id of the environment
name          |  string | uri | The name of the environment


## Response

`200 OK`

```bash
{
    "id": 1608,
    "log_export_schedule": null,
    "name": "production",
    "environment_name": "production",
    "state": "succeeded",
    "storage_directory": "/webroot/storage",
    "ssh_enabled": true,
    "trusted_ssh_ips": [
        "192.168.222.6"
    ],
    "maintenance_mode_enabled_at": null,
    "ssh_host": "b9cb804b63.x.vioengine.com",
    "ssh_port": 14462,
    "app_domain": "b9cb804b63.x.vioengine.com",
    "current_deployment_id": 10840,
    "container_root_directory": "/webroot",
    "app_type": "laravel",
    "auto_deploy_enabled": 1,
    "repo_owner": "amezmo",
    "repo_name": "demo.amezmo.com",
    "branch_name": "master",
    "provider_name": "GitHub",
    "maintenance_mode_enabled": false,
    "auto_install_composer": 1,
    "webroot": "/public",
    "app_domain_enabled": 1,
    "app_root": "/",
    "nginx_basic_auth_enabled": 0,
    "nginx_basic_auth_users": [],
    "trusted_ips": [],
    "node_modules_symlink": 0,
    "vendor_symlink": 0,
    "static_file_cache": 0,
    "auto_artisan_migrations": 1,
    "default_composer_version": "1",
    "auto_deploy_tag_patterns": [
        "v\\d+\\.\\d+\\.\\d+$"
    ],
    "auto_deploy_branch_patterns": [
        "feature/*"
    ],
    "newrelic_license_key": null
}
```
