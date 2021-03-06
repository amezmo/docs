# Logging

Your application code should be configured for writing logs to `/webroot/logs`. Because each deployment/release creates a new directory, your log files should be located outside of the application deployment directory. 
Logging to a directory outside of your deployment tree is the recommended way to peristent log files across deployments on Amezmo.

Recall the [deployment directory](/docs/deployments/directories) tree layout on Amezmo. By default,
the directory `/webroot/logs` is created for you when you launch an instance. We recommend using this directory
for logging. After setting up your application log directory from code,
you'll be able to see your logs from the Logs tab on Amezmo.

When you launch an instance, a default [.env](/docs/configuration/dotenv)
file is generated for you. The variable `LOG_DIRECTORY` is generated by default. You may use this variable to easily
port your code to different environments.

## Configuration for persistent logs
Laravel applications provide a logging configuration entry that you may change. The following configuration is recommended.
Laravel provides a [configuration path](https://laravel.com/docs/logging#customizing-monolog-for-channels) attribute
that lets you specify the directory to which your logs files should be written to.
See below for the recommended directory to use on Amezmo.

This following file is located at `app/config/logging.php`.

```php
return [
    'default' => 'stack',
    'channels' => [
        'daily' => [
            'driver' => 'daily',
            'permission' => 0664,
            'path' => env('LOG_PATH', '/webroot/logs/laravel.log'),
            'level' => 'debug',
            'days' => 14,
        ],
    ],

];
```

## Resources
- [How to: Persistent Logging For Laravel PHP Apps](https://www.amezmo.com/blog/persistent-logging-for-laravel-php-apps/)

