## Disable automatic Laravel migrations

Database migrations are run on each deployment if an `artisan` file is found in the root directory
of your application. You can disable automatic database migrations for Laravel applications.

## How to disable automatic Composer installations

- Open the Amezmo dashboard at [https://www.amezmo.com/sites](/sites)
- Choose the name of the application.
- Above the horizontal tab navigation menu, click the Production **or** Staging tab.
- In the horizontal tab navigation menu, choose the **Deployments** tab.
- Scroll down to the **Settings** section.
- Find the "Database migrations" switch

    <img src="https://s3.us-east-2.amazonaws.com/static.amezmo.net/laravel-migrations-switch.png" />
- Toggle the switch
    
After turning off Database migrations, your next deployment will not automatically run
`php artisan migrate`
