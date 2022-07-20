# Configuration

[DotEnv](https://github.com/vlucas/phpdotenv)
is a configuration pattern that loads environment variables from a `.env` file. Amezmo generates a
`.env` file for you at instance creation time.
This file is automatically available to you from your webroot.
Depending on the options you've chosen at instance creation time, you will see a set of predefined variables.

When a new deployment happens, the most recent `.env` file is copied into your deployments
target release directory.

Amezmo automatically generates a `.env` file for you when you launch an instance.
You can edit this file at anytime from the Configuration page.

Upon updating your configuration from the dashboard, the updates are immediately copied into your
[current release directory](/docs/deployments/directories).
Amezmo does not validate your file before placing it inside the root of your current release directory tree.

Your workers are reloaded via SIGHUP after your configuration file is copied into your release directory.

## Default variables
The following variables are automatically generated for you when you launch an instance.

| Variable      | Description
----------------|-------------
`APP_HOSTNAME`      | The hostname of the application environment
`STORAGE_DIRECTORY` | Path to the [persistent storage](/docs/configuration/storage) directory 
`LOG_DIRECTORY`     | This path can be used to persist log file across deployments
`NODE_ENV`          | Contains the application environment name

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

Amezmo provides the following Redis variables if your instance has Redis installed.

| Variable      | Description
----------------|-------------
`REDIS_HOST`        | The redis server IP address or hostname
`REDIS_PORT`        | Always 6379



## Hooks
Upon updating your configuration file, Amezmo will optionally execute a script on your behalf.

| Hook | Description
-------|------------
`.amezmo/config/before-change` | This script is executed before Amezmo places the updated configuration file into your current release directory
`.amezmo/config/after-change`  | This script is executed after the file was successfully copied to your current release directory, but before your workers are reloaded.


## Limits

- Configuration hooks have a 15 second timeout.
