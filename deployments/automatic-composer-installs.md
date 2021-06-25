# Automatic Composer package management

Upon connecting your Git repo, you have the option to automatically install your Composer packages. With this option checked, Amezmo
will check the top level directory of your repository for a composer.json file.
If one is found, then a composer install is executed. In addition, the following is also executed automatically in the order
listed below:

By default, Composer 1.x is used for automatic Composer installations. However, you may [change the default Composer version](/docs/how-to-guides/change-default-composer-version) for automatic composer installations.

```bash
composer --no-dev --no-ansi --no-interaction --optimize dump-autoload
```

Next, Amezmo determines if an `artisan` file exists in the root directory of the application. If it exists, then the following command 
is executed automatically. However, you may disable automatic Laravel migrations.

```bash 
php artisan migrate --no-interaction --no-ansi --force
```


## How-to Guides

- [How to change the default Composer version](/docs/how-to-guides/change-default-composer-version)
- [How to enable/disable automatic composer installations](/docs/how-to-guides/disable-automatic-composer-installs)
- [How to disable automatic Laravel migrations](/docs/how-to-guides/disable-automatic-laravel-migrations)