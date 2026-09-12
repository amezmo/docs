# Deployment Hooks

Amezmo will run a set of scripts for you before, during, and after your deployment.
These scripts are expected to be located in the `.amezmo` directory of your applications root directory.
The scripts are executed as a shell script using Bash.
A set of environment variables are given to the script, for your reference.
For example, the file [after.pull](after-pull.md)
is executed for the event After Pull.

## Hook files

Hooks are files.
In the below sample application directory structure, the `.amezmo` directory is where you define your "hook" scripts.

{title="Sample application directory structure"}
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

For directories, these are the permissions.

{title="Directory permissions"}
```sh
2775/drwxrwxr-x
```

For files, these are the permissions.

{title="File permissions"}
```sh
0664/-rw-rw--r--
```

## Hook list

The hooks run in the order below. Where a hook's exit status is honored, a
non-zero status fails the deployment.

### `before.pull`

Runs [before Amezmo fetches](before-pull.md) from your Git provider. Its exit
status is ignored.

### `after.pull`

Runs [after the fetch](after-pull.md). This is where you install Composer and
NPM dependencies. A non-zero exit status fails the deployment.

### `after.extract`

Runs after Amezmo extracts the archive from an
[API deployment](after-extract.md), so it applies to `.zip` deploys rather than
Git ones. A non-zero exit status fails the deployment.

### `before.deploy`

Runs [before your web server directory is updated](before-deploy.md), the last
point to act on the release before it goes live. A non-zero exit status fails
the deployment.

### `after.deploy`

Runs [once the web server directory points at the new release](after-deploy.md),
so your code is already live. Its exit status is ignored.

### `deploy.success`

The [last hook to run](deploy-success.md), after a successful deployment. Its
exit status is ignored.

### `deploy.failure`

Runs when [any hook or the deployment itself](deploy-failure.md) returns a
non-zero exit status.

## Environment File

Your [most recent .env file](../../configuration/dotenv.md), which is the one that you see in your
Amezmo Dashboard under the Configuration tab, is placed into the
newly created [deployment directory](../directories.md)
immediately completion of git pull.

This allows your hooks to use the contents of
the `.env` if you desire. However, the `.env` file loading does not happen automatically.
To accomplish this, simply edit your hook file to load it before doing anything else.

## Secrets

[Encrypted environment variables](../../secrets/index.md) are injected into the hooks environment
and exist in memory only.
You may access them inside your hook file using the bash syntax
for variables such as `$MY_SECRET_VARIABLE_NAME`.
Secrets will never be written to disk and only decrypted to execute hooks.

## Environment variables

Your hook script has access to the following pre-defined environment variables.
In addition to these environment variables, Amezmo injects your secret variables as well. For more
information about secrets, see the [Secrets Overview](../../secrets/index.md) page.

Variable   | Description
-----------|------------
APPLICATION_ROOT      | This is where your code is located on the server in the form of `deployment_${sequence_number}.${short_commit_id}`
COMMIT_ID             | Git commit hash of the currently executing deployment
NODE_PATH             | The path to the global node.js package binaries
COMPOSER_MEMORY_LIMIT | set to `-1`
PERSISTENT_STORAGE_DIRECTORY   | Path to the [persistent storage](../../configuration/storage.md) directory
APP_DOMAIN           | Internal domain name for the environment
REPO_NAME            | The name of the repository currently being deployed
DEPLOY_BRANCH        | The name of the branch currently being deployed
TARGET_HOOK          | The name of hook being executed. This is one of the values listed in the [Hook list](#hook-list)
RELEASE_NUMBER       | The generated release number. The value is in the form of `deployment_${sequence_number}.${short_commit_id}`
DEPLOYMENT_DIRECTORY | The fully qualified path to the current in progress deployment.
APP_TYPE             | The application type ID such as `drupal`, `laravel`, or `crafctms`
ENVIRONMENT_NAME     | The name of the [application environment](../../environments/index.md)

## Hook Monitoring

On the Deployments tab, you can see a list of your deployments.
To view a single deployment click on the link in the status column.
Note that, Amezmo will only show the hooks that were executed in the table below.

## Limits

- There is a 10 minute limit on hook execution
