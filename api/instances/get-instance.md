
# Get an instance

`GET` /v1/instances/{instance_id}


## Parameters
Parameter     |  Type | In    | Description     
------------- | ------|------ |------------------
instance_id   |  string | uri  | The instance id of the environment


## Response

`200 OK`

```bash
{
    "id": 1,
    "name": "engage-plugandplay-564192df9c",
    "runtime_description": "PHP",
    "instance_type": "business",
    "description": null,
    "runtime_config": {
        "php": {
            "max_upload_size_mb": 512,
            "fpm_worker_memory_limit_mb": 256,
            "version": "7.4"
        },
        "mysql": {
            "enabled": true,
            "version": "5.7"
        },
        "redis": {
            "enabled": true
        },
        "nginx": {
            "enabled": true
        }
    },
    "state": "Launching",
    "trusted_ssh_ips": [],
    "created_at": "2021-10-27T22:20:29.000000Z",
    "region": "x-us",
    "environments": [
        {
            "id": 1,
            "name": "production",
            "environment_name": "production",
            "state": "pending",
            "storage_directory": "/webroot/storage",
            "ssh_enabled": false,
            "maintenance_mode_enabled_at": null,
            "ssh_port": null,
            "app_domain": "564192df9c.lb2.example.com",
            "current_deployment_id": null,
            "container_root_directory": "/webroot",
            "app_type": null,
            "auto_deploy_enabled": 1,
            "repo_owner": null,
            "repo_name": null,
            "branch_name": null,
            "provider_name": null,
            "maintenance_mode_enabled": false,
            "auto_install_composer": 1,
            "webroot": null,
            "app_domain_enabled": 1,
            "app_root": null,
            "nginx_basic_auth_enabled": 0,
            "nginx_basic_auth_users": [],
            "trusted_ips": [],
            "node_modules_symlink": 0,
            "vendor_symlink": 0,
            "static_file_cache": 0,
            "auto_artisan_migrations": 1,
            "default_composer_version": "1",
            "auto_deploy_tag_patterns": [],
            "auto_deploy_branch_patterns": []
        },
        {
            "id": 2,
            "name": "staging",
            "environment_name": "staging",
            "state": "pending",
            "storage_directory": "/webroot/3ee35a7060676b6d/storage",
            "ssh_enabled": false,
            "maintenance_mode_enabled_at": null,
            "ssh_port": null,
            "app_domain": "3ee35a7060676b6d.lb2.example.com",
            "current_deployment_id": null,
            "container_root_directory": "/webroot/3ee35a7060676b6d",
            "app_type": null,
            "auto_deploy_enabled": 1,
            "repo_owner": null,
            "repo_name": null,
            "branch_name": null,
            "provider_name": null,
            "maintenance_mode_enabled": false,
            "auto_install_composer": 1,
            "webroot": null,
            "app_domain_enabled": 1,
            "app_root": null,
            "nginx_basic_auth_enabled": 0,
            "nginx_basic_auth_users": [],
            "trusted_ips": [],
            "node_modules_symlink": 0,
            "vendor_symlink": 0,
            "static_file_cache": 0,
            "auto_artisan_migrations": 1,
            "default_composer_version": "1",
            "auto_deploy_tag_patterns": [],
            "auto_deploy_branch_patterns": []
        }
    ]
}
```
