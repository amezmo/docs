# Deployment Hooks

Amezmo will run a set of scripts for you before, during, and after your deployment.
These scripts are expected to be located in the `.amezmo` directory of your applications root directory.
The scripts are executed as a shell script using Bash.
A set of environment variables are given to the script, for your reference.
For example, the file [after.pull](/docs/deployments/hooks/after-pull)
is executed for the event After Pull.

## Hook files

Hooks are files.
In the below sample application directory structure, the `.amezmo` directory is where you define your "hook" scripts.


```bash
# A sample laravel application root directory.
# The `tree -a -L 2 .` command was run inside a Laravel app's root directory.
.
├── .amezmo
│   ├── after.deploy
│   ├── after.pull
│   ├── after.extract
│   ├── before.deploy
│   ├── after.deploy
│   ├── deploy.failure
│   └── deploy.success
├── app
├── artisan
├── bootstrap
├── composer.json
├── composer.lock
├── config
├── database
├── routes
├── server.php
├── storage
├── vendor
├── node_modules
├── .env
```

As part of the deployment process, Amezmo will run a chmod across your target deployment directory after hooks run. This ensures that
any files created from your hooks will have correct and expected permissions. Amezmo ensures the owner/group is
`www-data:deployer`. This allows for expected permissions across all areas of your application.


For directories, the permissions are `2775/drwxrwxr-x`, for files the permissions are `0664/-rw-rw--r--`.

## Hook list

- [before.pull](/docs/deployments/hooks/before-pull)
- [after.pull](/docs/deployments/hooks/after-pull)
- [after.extract](/docs/deployments/hooks/after-extract)
- [before.deploy](/docs/deployments/hooks/before-deploy)
- [after.deploy](/docs/deployments/hooks/after-deploy)
- [deploy.success](/docs/deployments/hooks/deploy-success)
- [deploy.failure](/docs/deployments/hooks/deploy-failure)

## Environment file

The [most recent .env file](/docs/configuration/dotenv), which is the one that you see in the dashboard within the Configuration tab,
is placed into the newly created [deployment directory](/docs/deployments/directories) immediately completion of git pull.
This allows your hooks to use the contents of the `.env` if you desire.
However, the `.env` file loading does not happen automatically.
To accomplish this, simply edit your hook file to load it before doing anything else.

## Secrets

[Encrypted environment variables](/docs/secrets) are injected into the hooks environment
and exist in memory only.
You may access them inside your hook file using the bash syntax
for variables such as `$MY_SECRET_VARIABLE_NAME`.
Secrets will never be written to disk and only decrypted to execute hooks.

## Environment variables

Your hook script has access to the following pre-defined environment variables.
In addition to these enviroment variables, Amezmo injects your secret variables as well. For more
information about secrets, see the [Secrets Overview](/docs/secrets) page.

| Variable              | Description |
| ----------------------|------------ |
| APPLICATION_ROOT      | This is where your code is located on the server in the form of `deployment_${sequence_number}.${short_commit_id}` |
| COMMIT_ID             | Git commit hash of the currently executing deployment |
| NODE_PATH             | The path to the global node.js package binaries |
| COMPOSER_MEMORY_LIMIT | set to `-1` |
| PERSISTENT_STORAGE_DIRECTORY | Path to the [persistent storage](/docs/configuration/storage) directory |
| APP_DOMAIN           | Internal domain name for the environmnt |
| REPO_NAME            | The name of the repository currently being deployed |
| DEPLOY_BRANCH        | The name of the branch currently being deployed |
| TARGET_HOOK          | The name of hook being executed. This is one of the values listed in the [Hook list](/docs/deployments/hooks/#hook-list) |
| RELEASE_NUMBER       | The generated release number. The value is in the form of `deployment_${sequence_number}.${short_commit_id}` |
| DEPLOYMENT_DIRECTORY | The fully qualified path to the current in progress deployment. |
| APP_TYPE             | The application type ID such as `drupal`, `laravel`, or `crafctms` |
| ENVIRONMENT_NAME     | The name of the [application environment](/docs/environments) |
| PUBLIC_DOCUMENT_ROOT | This value represents the public facing entry point of your application which is where index.php located. It is the same value that you setup with your Git integration, and under your Nginx tab. |

## Hook Monitoring

On the Deployments tab, you can see a list of your deployments.
To view a single deployment click on the link in the status column.
Note that, Amezmo will only show the hooks that were executed in the table below.

## Limits

- There is a 10 minute limit on hook execution
