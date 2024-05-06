# Configuration

[PHP dotenv](https://github.com/vlucas/phpdotenv)
is a library that loads your variables from a `.env` and puts them in your
PHP runtime environment. These variables are usually read from your
[`$_SERVER`](https://www.php.net/manual/en/reserved.variables.server.php)
or [`$_ENV`](https://www.php.net/manual/en/reserved.variables.environment.php)
[superglobal](https://www.php.net/manual/en/language.variables.superglobals.php)
variables.

Amezmo generates a
`.env` file for you at instance creation time.
This file is automatically available to you from your [webroot](/docs/deployments/directories). Depending on the options you've chosen at instance creation time,
you will see a set of predefined variables.

When your [deployment] is triggered, the most recent `.env` file is copied
into your deployment [target release directory](/docs/deployments/directories).

Upon updating your configuration from the dashboard,
the updates are immediately copied into your
[current release directory](/docs/deployments/directories).
Amezmo does not validate your file before placing it inside
the root of your current release directory tree.

After your new configuration variables are copied into your
[release directory](/docs/deployments/releases),
your [workers are restarted](/docs/workers/reloading) via `SIGHUP`
automatically.

## Amezmo Generated Variables
The following variables are automatically generated for you whenever you
[create a site](/docs/instances).

| Variable      | Description
----------------|-------------
`APP_HOSTNAME`      | The hostname of the application environment
`STORAGE_DIRECTORY` | Path to the [persistent storage](/docs/configuration/storage) directory
`LOG_DIRECTORY`     | This path can be used to persist log file across deployments
`NODE_ENV`          | Contains the application environment name
`AMEZMO_ENVIRONMENT` | The environment name

Amezmo provides the following database variables if your instance has MySQL installed.

| Variable      | Description
----------------|-------------
`DB_PORT`           | Always 3306
`DB_USERNAME`       | Database username that was provided during instance creation
`DB_HOST`           | Contains the hostname of your MySQL server
`DB_PASSWORD`       | Database password
`DB_DATABASE`       | Default database name
`DB_VENDOR`         | Always MySQL
`DB_VERSION`        | The version number of MySQL in major.minor.patch form

Amezmo provides the following [Redis](https://redis.io) variables
if your instance has Redis installed.

| Variable      | Description
----------------|-------------
`REDIS_HOST`        | The redis server IP address or hostname
`REDIS_PORT`        | Always 6379


## Environment Variable Hooks
Upon updating your DotEnv Configuration file,
Amezmo will search for hooks

| Hook | Description
-------|------------
`.amezmo/config/before-change` | This script is executed before Amezmo places the updated configuration file into your current release directory
`.amezmo/config/after-change`  | This script is executed after the file was successfully copied to your current release directory, but before your workers are reloaded.


## Limits

- Configuration hooks have a 15 second timeout.
