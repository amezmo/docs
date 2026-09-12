# PHP

PHP on Amezmo comes with FastCGI Process Manager (<abbr title="FastCGI Process Manager">FPM</abbr>) and the PHP command line. The common extensions you
expect are installed by default, so you can focus on your code, not
configuration.

## In This Section

### PHP Versions

Choose a [PHP version](versions.md) at launch and change it later. It applies to
both FPM and the command line, so your web requests and scripts run the same
PHP.

### Extensions

The [common extensions](extensions.md) ship installed, so most applications run
without extra setup. There is no per-application install step.

### Composer

Every PHP instance has [both Composer versions installed](composer.md), as the
`composer` and `composer2` commands, for use in deployment hooks or over SSH.
