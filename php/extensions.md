# PHP Extensions

Amezmo instances ship with the common PHP extensions already installed, so most
apps run without extra setup. There is no per-app install step for extensions.

## Installed by Default

- zip
- imagick
- sqlite
- mysql
- mbstring
- tokenizer
- xml
- ctype
- json
- bcmath
- gd
- curl
- soap
- intl
- imap

Redis is available too, through the phpredis extension. So imagick, sqlite and
Redis are ready to use with nothing to install.

## Something Not in the List

If your app needs an extension that isn't installed, contact support. The
platform can provision extra extensions for your instance.

## New Relic

New Relic APM isn't a PHP extension you install. It's a feature of
dedicated-memory plans. On a qualifying plan, turn it on by setting a
``newrelic_license_key`` environment variable with your New Relic license key.
