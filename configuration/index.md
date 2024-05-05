# Configuration

Amezmo automates configuration for
your application based on your framework.
When [connecting a git repo](/docs/git),
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

The [webroot](/docs/configuration/public-directory), or public document
root is a directory within your application in which
files within it are served directly by the [web server](/docs/nginx).
This usually has your `index.php` file and static assets.

## Environment Variables

Amezmo generates your server [environment variables](/docs/configuration/dotenv) automatically.

## Logging

You can use the persistent storage on your instance
for [logging](/docs/configuration/logging)

## Persistent Storage
Keep your user uploaded content available between
[deployments](/docs/deployments) by configuring your PHP app
to write to a [persistent storage directory](/docs/configuration/storage).
Amezmo has a set of recommendations on how to configure
your application settings for best performance.
