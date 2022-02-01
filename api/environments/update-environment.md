
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

When updating `newrelic_license_key`, the change takes effect on the next [deployment](/docs/api/deployments). Providing a `null` value disables 
the New Relic APM integration. When you provide your New Relic API key, Amezmo encrypts the value at rest. The value is decrypted upon instance creation and is stored in the `newrelic.ini` PHP configuration file. You may see the value by running `php --ri newrelic | grep newrelic.license`

Note that New Relic is only supported with Advanced instances. See [instance types](/docs/api/instances/list-instance-types).

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
    "auto_deploy_tag_patterns": [
        "v\\d+\\.\\d+\\.\\d+$"
    ],
    "auto_deploy_branch_patterns": [
        "feature/*"
    ],
    "newrelic_license_key": "YES"
}
```
