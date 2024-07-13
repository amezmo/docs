# Amezmo Documentation

Welcome to Amezmo. This documentation is continuously refined and updated
by the Amezmo community. With that being said, Amezmo welcomes all
contributions on the public [Amezmo Docs](https://github.com/amezmo/docs) repo.

## How PHP Hosting Works On Amezmo
on Amezmo, your production sites will sustain uninterupted availibility
at all times. First, you must have be using `Git` with either Github, BitBucket,
or GitLab. Secondly, your applications must be able to run outside your local
machine. That is, your application should not be hardcoded to depend on
a personal file or directory.

Your PHP applications on Amezmo execute in a homogeneous server environment.
Your application is deployed with [Atomic PHP Deployments](/docs/deployments).
Out of the box, your application should run without requiring custom packages.
Amezmo creates a Docker image based on Ubuntu in advance with the
most common update-to-date packages. For special requirements, please send us a
message on [Slack](https://wwww.amezmo.com/goslack), or support,
and we'll customize your image to install any custom packages with
[Apt](https://manpages.ubuntu.com/manpages/xenial/man8/apt-get.8.html).

## Amezmo PHP Hosting Components for Your Applications
Get details about setting up your PHP applications and server infrastructure on Amezmo. Learn about
automated deployments, and more. For specific questions that are not answered here, we encourage you to join us on [Slack](/goslack).

### Instances
Launch a dedicated service instance, or a full stack instance. Scale up or down at anytime.
[Learn more](/docs/instances).

### Databases
Run a fully managed dedicated instance of MySQL on Amezmo. Launch a database instance
into your private network and let your other instances connect to it.
[Learn more](/docs/databases).

### Deployments
Automatically deploy your PHP application with zero-downtime using Git.
[Learn more](/docs/deployments).


### See Also
- [YouTube](https://www.youtube.com/@amezmo6464)
- [GitHub](https://www.github.com/amezmo)
- [PHP hosting Guides](https://www.amezmo.com/guides)
- [Drupal hosting guide](https://www.amezmo.com/guides/deploy-a-drupal-site-on-amezmo)
- [Laravel Github Actions Guide](https://www.amezmo.com/laravel-hosting-guides/deploying-laravel-with-github-actions)
- [Headless Craft CMS with NextJS](https://www.amezmo.com/craft-cms-hosting-guides/how-to-set-up-a-headless-craft-cms-with-nextjs)