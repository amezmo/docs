# Instances

Applications on Amezmo run in an optimized Docker container instance. Each
instance is an isolated container on reserved hardware, built to run PHP apps.
Launching an instance creates one container with a staging environment and a
production environment. Both environments live in the same container, and every
action in the dashboard runs in the context of one environment.

Everything you need to run a production PHP app is set up by default, with
little or no custom configuration. Amezmo includes framework-specific
configuration for CraftCMS, Laravel, and Yii.

For pricing and features, see the [pricing](/pricing) page.

## Managing Instances

### Scaling

[Scale an instance](scaling.md) up when you need more memory or computing
power, or back down afterward.

### Pausing

[Pausing](pausing.md) takes an instance offline without deleting it. It shuts
down and stops accepting requests, and you can start it again.

### Terminating

[Terminating](terminating.md) removes an application from Amezmo permanently.
Pause instead if you only need it offline for a while.

### Sharing

[Sharing](sharing.md) joins your instance to another instance's private network
and gives it an address inside that network.

### Enable or Disable SSH

Toggle [SSH access](enable-or-disable-ssh.md) from the Overview tab. With it
off, the instance doesn't answer SSH at all.

### SSH Access

[SSH](ssh.md) runs through a secure entry-point host that routes you from the
load balancer to your instance on a pre-allocated port.

### SSH Troubleshooting

[SSH troubleshooting](ssh-troubleshooting.md) covers connection failures,
particularly "Permission denied (publickey)".

### Trusted IP Addresses

Restrict which machines can open an SSH connection with
[trusted IP addresses](trusted-ip-addresses.md). These apply to SSH only, not to
web traffic.

### Ports and IP Addresses

Amezmo leaves the [default ports](ports-and-ip-addresses.md) in place for Nginx,
MySQL, and Redis.

### Instance Limits

Your account can run a [set number of applications](limits.md) at once. The
limit starts low on a new account and rises as the account establishes itself.

### Regions

Your [region](regions.md) sets where the application runs. Amezmo defaults to
North America and you can change it on the launch screen.

### Troubleshooting

[Instance troubleshooting](troubleshooting.md) covers a launch that is refused
or seems to stall.

## Features

- MySQL 5.7 and 8.0
- Nginx
- Redis
- Node.js, [NPM](../npm/index.md) and Yarn
- Optimized PHP-<abbr title="FastCGI Process Manager">FPM</abbr> (FastCGI Process Manager)
- Composer and [Composer 2](../php/composer.md)
- [Development subdomain](../domains/development-subdomain.md)
- Staging environments
- Custom domains with SSL
- Managed background workers
- Managed Cron jobs

Amezmo instances are locked down by default, with no root access. That's by
design: it helps you and the Amezmo team keep a secure, predictable environment
for running PHP apps.
