# Logging

{.lead}
Your application writes logs to `/webroot/logs`. Each deployment creates a new
release directory, so log files kept inside the application tree disappear on
the next deploy. Writing to `/webroot/logs`, which sits outside the release
tree, keeps your logs **persistent** across deployments.

Amezmo creates `/webroot/logs` when you launch an instance. See the
[deployment directory](../deployments/directories.md) layout for where it sits.
Once your application writes to this directory, its logs appear on the Logs tab
in the Amezmo Dashboard.

Amezmo also generates a `LOG_DIRECTORY` variable in the default
[.env](dotenv.md) file, so you can point your logging configuration at the
directory without hard-coding the path across environments.

## Configuration for Persistent Logs

Laravel exposes a logging configuration you can change to write logs to the
persistent directory. A Laravel channel takes a
[path attribute](https://laravel.com/docs/logging#customizing-monolog-for-channels)
that sets the log file location. The following `config/logging.php` defines a
daily channel that writes to `/webroot/logs`.

{title="config/logging.php"}
```php
return [
    'default' => 'stack',
    'channels' => [
        'daily' => [
            'driver' => 'daily',
            'permission' => 0664,
            'path' => env('LOG_DIRECTORY', '/webroot/logs') . '/laravel.log',
            'level' => 'debug',
            'days' => 14,
        ],
    ],
];
```

## Resources

- [How to: Persistent Logging for Laravel PHP Apps](https://www.amezmo.com/blog/persistent-logging-for-laravel-php-apps/)
