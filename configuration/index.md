# Configuration

{.lead}
Amezmo **configures** your application automatically based on its framework.
When you [connect a git repo](../git/index.md), you choose your application
type, and Amezmo applies the web server and runtime settings that match it.

## Supported PHP Frameworks

Amezmo detects and configures these frameworks:

- Backdrop
- Bedrock
- Craft CMS
- Drupal
- Laravel
- Laravel Octane
- PHP
- Symfony
- WordPress

## Public Document Root

The [public document root](public-directory.md) is the directory the
[web server](../nginx/index.md) serves files from directly. It holds your
`index.php` file and static assets. Amezmo sets it from your framework, and you
can change it.

## Environment Variables

Amezmo generates your [environment variables](dotenv.md) automatically and
writes them to a `.env` file when you launch an instance.

## Logging

Your instance keeps a directory for [log files](logging.md) that sits outside
the release tree, so your logs stay available across deployments.

## Persistent Storage

A [persistent storage directory](storage.md) keeps user uploaded content
available across [deployments](../deployments/index.md). You configure your PHP
application to read and write files there.
