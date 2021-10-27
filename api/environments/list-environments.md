
# List environments

`GET` /v1/{instanceId}/environments

## Parameters
Parameter     |  Type | In    | Description     
------------- | ------|------ |------------------
instanceId    |  string | uri  | The instance id

## Response

`200 OK`

```bash
[
    {
        "id": 1,
        "environment_name": "production",
        "state": "pending",
        "storage_directory": "/webroot/production/storage",
        "ssh_enabled": false,
        "maintenance_mode_enabled_at": null,
        "ssh_port": null,
        "app_domain": "production.example.com",
        "current_deployment_id": null,
        "container_root_directory": "/webroot/production",
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
        "environment_name": "staging",
        "state": "pending",
        "storage_directory": "/webroot/staging/storage",
        "ssh_enabled": false,
        "maintenance_mode_enabled_at": null,
        "ssh_port": null,
        "app_domain": "staging.example.com",
        "current_deployment_id": null,
        "container_root_directory": "/webroot/staging",
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
```
