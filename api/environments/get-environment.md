
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
    "id": 24242424242424,
    "name": "production",
    "environment_name": "production",
    "state": "pending",
    "storage_directory": "/webroot/98b69b41fe1b8991/storage",
    "ssh_enabled": false,
    "maintenance_mode_enabled_at": null,
    "ssh_port": null,
    "app_domain": "98b69b41fe1b8991.example.com",
    "current_deployment_id": null,
    "container_root_directory": "/webroot/98b69b41fe1b8991",
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
```
