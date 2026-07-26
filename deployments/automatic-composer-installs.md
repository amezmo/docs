# Automatic Composer Package Management

When you connect your Git repo, you can have Amezmo install your Composer
packages on every deployment. With this option on, Amezmo checks the top level
directory of your repository for a ``composer.json`` file. If it finds one, it
runs ``composer install``, then dumps an optimized autoloader:

```bash
$ composer --no-dev --no-ansi --no-interaction --optimize dump-autoload
```

Composer 1.x runs these commands by default. You can
[change the default Composer version](../how-to-guides/change-default-composer-version.md)
per environment. See [Composer](../php/composer.md) for the difference between
``composer`` and ``composer2``.

Next, Amezmo checks for an ``artisan`` file in the root directory. If it finds
one, it runs your database migrations:

```bash
$ php artisan migrate --no-interaction --no-ansi --force
```

You can turn either step off. See the how-to guides below.

## What Doesn't Run Automatically

Amezmo runs only the two commands above. It does not run any other Artisan
command for you, so caching commands like ``config:cache``, ``route:cache``, or
``cache:clear`` are yours to run. Put them in a
[deployment hook](hooks/index.md) such as ``after.pull`` when you need them.

## How-to Guides

- [Change the default Composer version](../how-to-guides/change-default-composer-version.md)
- [Enable or disable automatic Composer installs](../how-to-guides/disable-automatic-composer-installs.md)
- [Disable automatic Laravel migrations](../how-to-guides/disable-automatic-laravel-migrations.md)
