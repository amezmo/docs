# Instances

Applications on Amezmo run in an optimized Docker container instance. Each
instance is an isolated container on reserved hardware, built to run PHP apps.
Launching an instance creates one container with a staging environment and a
production environment. Both environments live in the same container, and every
action in the dashboard runs in the context of one environment.

Everything you need to run a production PHP app is set up by default, with
little or no custom configuration. Amezmo includes framework-specific
configuration for CraftCMS, Laravel and Yii.

For pricing and features, see the [pricing](/pricing) page.

## Managing Instances

- [Scaling](scaling.md)
- [Pausing](pausing.md)
- [Terminating](terminating.md)
- [Sharing](sharing.md)
- [Enable or disable SSH](enable-or-disable-ssh.md)
- [SSH access](ssh.md)
- [SSH troubleshooting](ssh-troubleshooting.md)
- [Trusted IP addresses](trusted-ip-addresses.md)
- [Ports and IP addresses](ports-and-ip-addresses.md)
- [Instance limits](limits.md)
- [Regions](regions.md)
- [Troubleshooting](troubleshooting.md)

## Features

- MySQL 5.7 and 8.0
- Nginx
- Redis
- Node.js, [NPM](../npm/index.md) and Yarn
- Optimized PHP-FPM
- Composer and [Composer 2](../php/composer.md)
- [Development subdomain](../domains/development-subdomain.md)
- Staging environments
- Custom domains with SSL
- Managed background workers
- Managed Cron jobs

Amezmo instances are locked down by default, with no root access. That's by
design: it helps you and the Amezmo team keep a secure, predictable environment
for running PHP apps.
