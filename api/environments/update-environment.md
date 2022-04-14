
# Update an environment

```bash
PATCH /v1/instances/{instance_id}/environments/{name}/production
```

## Parameters
Parameter     |  Type | In    | Description     
------------- | ------|------ |------------------
instance_id    |  string | uri  | The instance id of the environment
name          |  string | uri | The name of the environment. See [environments](/docs/api/environments/list-environments)
auto_deploy_tag_patterns | array | body | An array of regular expressions to match a git tag
auto_deploy_branch_patterns | array | body | An array of of regular expressions to match a git branch.
newrelic_license_key | string | body | [New Relic API key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/)
ssh_enabled | bool | body | 
trusted_ssh_ips | array | body | an array of IPv4 addresses


When updating `newrelic_license_key`, the change takes effect on the next [deployment](/docs/api/deployments). Providing a `null` value disables 
the New Relic APM integration. When you provide your New Relic API key, Amezmo encrypts the value at rest. The value is decrypted upon instance creation and is stored in the `newrelic.ini` PHP configuration file. You may see the value by running `php --ri newrelic | grep newrelic.license`

Note that New Relic is only supported with Advanced instances. See [instance types](/docs/api/instances/list-instance-types).

When patching `ssh_enabled` to be false, `trusted_ssh_ips` is reset to an emtpy array.


## Code samples
```bash
curl https://api.amezmo.com/v1/instances/{instanceId}/environments/production -X PATCH \
    -H 'Authorization: Bearer {api_key}' \
    --data auto_deploy_tag_patterns[]='v\d+\.\d+\.\d+$'
```

## Response

```bash
200 OK
```

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
