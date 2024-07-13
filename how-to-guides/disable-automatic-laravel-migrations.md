# Disable automatic Laravel migrations

Database migrations are run on each deployment if an `artisan` file is found in the root directory
of your application. You can disable automatic database migrations for Laravel applications.

## How to disable automatic Composer installations

1. Open the Amezmo dashboard at [https://www.amezmo.com/sites](/sites)
2. Choose the name of your application.
3. Above the horizontal tab navigation menu, click the Production **or** Staging tab.
4. In the horizontal tab navigation menu, choose the **Deployments** tab.
5. Scroll down to the **Settings** section.
6. Find the "Database migrations" switch

    <img class="img-enlargable" src="https://s3.us-east-2.amazonaws.com/static.amezmo.net/laravel-migrations-switch.png" />
7. Toggle the switch

After turning off Database migrations,
your next [deployment](/docs/deployments) will not automatically run `php artisan migrate`
