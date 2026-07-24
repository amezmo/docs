# Configuration

Amezmo automates configuration for
your application based on your framework.
When [connecting a git repo](../git/index.md),
you can choose your application type.

## Supported PHP Frameworks

- Backdrop
- Bedrock
- Craft CMS
- Drupal
- Laravel
- Laravel Octane
- PHP
- Symfony
- Wordpress

## Public Document Root

The [webroot](public-directory.md), or public document
root is a directory within your application in which
files within it are served directly by the [web server](../nginx/index.md).
This usually has your `index.php` file and static assets.

## Environment Variables

Amezmo generates your server [environment variables](dotenv.md) automatically.

## Logging

You can use the persistent storage on your instance
for [logging](logging.md)

## Persistent Storage
Keep your user uploaded content available between
[deployments](../deployments/index.md) by configuring your PHP app
to write to a [persistent storage directory](storage.md).
Amezmo has a set of recommendations on how to configure
your application settings for best performance.
