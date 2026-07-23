# The .env File

[PHP dotenv](https://github.com/vlucas/phpdotenv) loads your variables from a
``.env`` file into the PHP runtime, where your code reads them from the
[``$_SERVER``](https://www.php.net/manual/en/reserved.variables.server.php) or
[``$_ENV``](https://www.php.net/manual/en/reserved.variables.environment.php)
[superglobals](https://www.php.net/manual/en/language.variables.superglobals.php).

Amezmo generates a ``.env`` file for you when you create an instance, available
from your [webroot](../deployments/directories.md). It contains a set of
predefined variables based on the options you chose at instance creation.

When a [deployment](../deployments/index.md) runs, Amezmo copies the most recent
``.env`` file into the [target release directory](../deployments/directories.md).
When you update your configuration from the dashboard, Amezmo copies those
changes into your [current release directory](../deployments/directories.md)
right away. Amezmo does not validate the file before placing it in the root of
your current release directory.

After the new variables are in your
[release directory](../deployments/releases.md), Amezmo
[reloads your workers](../workers/reloading.md) with ``SIGHUP`` automatically.

## Amezmo-Generated Variables

Amezmo generates these variables whenever you
[create a site](../instances/index.md).

| Variable             | Description |
| -------------------- | ----------- |
| `APP_HOSTNAME`       | The hostname of the application environment |
| `STORAGE_DIRECTORY`  | Path to the [persistent storage](storage.md) directory |
| `LOG_DIRECTORY`      | This path can be used to persist [log files](logging.md) across deployments |
| `NODE_ENV`           | Contains the application environment name |
| `AMEZMO_ENVIRONMENT` | The environment name |

Amezmo provides these database variables if your instance has MySQL installed.

| Variable      | Description |
| ------------- | ----------- |
| `DB_PORT`     | Always 3306 |
| `DB_USERNAME` | Database username provided during instance creation |
| `DB_HOST`     | Hostname of your MySQL server |
| `DB_PASSWORD` | Database password |
| `DB_DATABASE` | Default database name |
| `DB_VENDOR`   | Always MySQL |
| `DB_VERSION`  | The MySQL version in major.minor.patch form |

Amezmo provides these [Redis](https://redis.io) variables if your instance has
Redis installed.

| Variable     | Description |
| ------------ | ----------- |
| `REDIS_HOST` | The Redis server IP address or hostname |
| `REDIS_PORT` | Always 6379 |

## Environment Variable Hooks

When you update your ``.env`` configuration, Amezmo looks for these hooks:

| Hook                           | Description |
| ------------------------------ | ----------- |
| `.amezmo/config/before-change` | Runs before Amezmo places the updated file into your current release directory |
| `.amezmo/config/after-change`  | Runs after Amezmo copies the file to your current release directory, before your workers reload |

## Limits

- Configuration hooks have a 15 second timeout.

## See Also

- [Secrets](../secrets/how-secrets-work.md)
