# Update an environment

{.lead}
Update the settings of an **environment** on an instance, such as auto-deploy
patterns, SSH access and the New Relic license key.

`PATCH` /v1/instances/{instance_id}/environments/{name}

## Parameters for "Update an environment"

Parameter | Type | In | Description
--------- | ---- | -- | -----------
instance_id | string | uri | **Required** The instance id
name | string | uri | **Required** The environment name. See [List environments](list-environments.md)
auto_deploy_tag_patterns | array | body | Regular expressions that match a git tag
auto_deploy_branch_patterns | array | body | Regular expressions that match a git branch
newrelic_license_key | string | body | [New Relic API key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/)
ssh_enabled | boolean | body | Enables or disables SSH access for the environment
trusted_ssh_ips | array | body | An array of IPv4 addresses allowed to connect over SSH

When you update `newrelic_license_key`, the change takes effect on the next
[deployment](../deployments/index.md). A `null` value disables the New Relic APM
integration. Amezmo encrypts the key at rest, decrypts it at instance creation
and stores it in the `newrelic.ini` PHP configuration file. You can read the
stored value with `php --ri newrelic | grep newrelic.license`.

Amezmo supports New Relic only on Advanced instances. See
[instance types](../instances/list-instance-types.md).

When you set `ssh_enabled` to `false`, Amezmo resets `trusted_ssh_ips` to an
empty array.

## Code samples for "Update an environment"

### Request example

{title="PATCH /v1/instances/{instance_id}/environments/{name}"}
```bash
curl https://api.amezmo.com/v1/instances/{instance_id}/environments/production \
    -X PATCH \
    -H "Authorization: Bearer $AMEZMO_API_KEY" \
    --data auto_deploy_tag_patterns[]='v\d+\.\d+\.\d+$'
```

### Response

{title="200 OK"}
```javascript
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
    "ssh_host": "b9cb804b63.lb2.example.com",
    "ssh_port": 14462,
    "app_domain": "b9cb804b63.lb2.example.com",
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
