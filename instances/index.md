# Instances

Applications on Amezmo are backed by an optimzed Docker container instance. Each "instance" of an application
is a isolated container running on reserved hardware resources. Amezmo was designed to run PHP apps. Launching an instance
on Amezmo creates a single container instance with two environments

Developer, and Business instances come with a staging environment and a production environment by default. These environments
are located within the same container instance. Each operation on the Amezmo dashboard operates with an environment
context.

All of the configuration required to run a production-ready PHP app is ready by default with little or no custom
configuration required. Our system supports framework-specific configurations for frameworks such as CraftCMS, Laravel, and Yii.

For pricing and features, see the [pricing](/pricing) page.

## Features

- MySQL 5.7, and 8.0
- Nginx
- Redis
- Node.js, [NPM](/docs/npm), and Yarn
- Optimized PHP-FPM
- Composer and [Composer 2](/docs/php/composer)
- [Development subdomain](/docs/domains/development-subdomain)
- Staging environments
- Custom domains with SSL
- Managed background workers
- Managed Cron jobs

Amezmo is designed to be "locked down" by default. This means no root access. This is by design, and
helps you, and the Amezmo team maintain a secure, and predictable environment for running PHP apps.
