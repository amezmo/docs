# Disable Automatic Laravel Migrations

Amezmo runs your database migrations on each deployment when it finds an
``artisan`` file in your application's root directory. You can turn off
automatic migrations for Laravel applications.

## Disabling Automatic Laravel Migrations

1. Open the Amezmo dashboard at [https://www.amezmo.com/sites](/sites)
2. Choose the name of your application.
3. Above the horizontal tab navigation menu, click the Production **or**
   Staging tab.
4. In the horizontal tab navigation menu, choose the **Deployments** tab.
5. Scroll down to the **Settings** section.
6. Find the "Database migrations" switch.

    ![Deployments Settings section with the Database migrations switch.](https://s3.us-east-2.amazonaws.com/static.amezmo.net/laravel-migrations-switch.png){.img-enlargable}
7. Toggle the switch.

After you turn off Database migrations, your next
[deployment](../deployments/index.md) will not run ``php artisan migrate``.
