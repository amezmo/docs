
# Create an instance

`POST` /v1/instances

## Parameters
Parameter     |  Type   | In    | Description     
---------------| --------|------ |------------------
runtime        | string     | body  | **Required** One of `php`, `mysql`, `dotnet`
instance_type  | string     | body  | **Required**  One of `hobby`, `developer`, `business`. See [Instance types](/docs/api/instances/list-instance-types)
region         | string     | body  | **Required**  The region id. See [Regions](/docs/api/regions/list-regions)
name           | string     | body | The identifier for this instance.
domain         | string     | body | An initial domain name for the production environment
php            | dictionary | body | PHP configuration. Only valid if `runtime` is `php`
php.version           | string     | php | The PHP version for the instance
php.composer_version  | string | php | The default [composer](https://getcomposer.org) version. Either `1` or `2`
mysql          | dictionary | body | MySQL configuration
mysql.version  | string  | mysql | `5.7` or `8`
mysql.enabled  | boolean | mysql | Enables or disables the MySQL server for this instance.
mysql.database    | dictionary | mysql | Initial database configuration
mysql.database.name | string | mysql.database | Initial database name
mysql.database.user | string | mysql.database | Initial database user
mysql.database.password | string | mysql.database | Initial database password


## Code samples

```bash
curl https://api.amezmo.com/v1/instances -X POST -H 'Authorization: Bearer {api_key}' \
    --data runtime=php
    --data instance_type=business
    --data region=lb2-us
```

## Response

`201 Created`

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
    "region": "lb2-us",
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
