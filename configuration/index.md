# Configuration

Amezmo provides configuration options and recommendations for your application based on your application type.
Upon [importing a repo](/docs/git), you can choose your application type. The following app types are
officially supported on Amezmo.

- Laravel
- Symfony
- Craft CMS
- Generic PHP

## Public document root

Define where your application should have its files served from and set up a
symbolic link to a persistant storage directory for publicly accessible file uploads.
[Learn more](/docs/configuration/public-directory)

## Environment Variables

Modify your Environment Variables from the dashboard. [Learn more](/docs/configuration/dotenv)

## Logging
Logging to a dedicated directory is recommended to keep log files across deployments.
[Learn more](/docs/configuration/logging)

## Storage
Keep your user uploaded content available across deployments by configuring your PHP app
to write to a dedicated storage directory. Amezmo has a set of recommendations on how to configure
your application settings for best performance.
[Learn more](/docs/configuration/storage)
