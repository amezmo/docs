# Setting up the storage directory

The storage directory must persist between deployments. Storage directories commonly store user uploaded data. You may configure your application
to run a [before.deploy](../deployments/hooks/after-pull.md) script to setup your storage directory. See below for complete example scripts.

To create a [persistent storage directory](../configuration/storage.md), copy the script from one of the links below.

## Laravel

- [Github Script](https://github.com/amezmo/demo.amezmo.com/blob/master/.amezmo/before.deploy)


## Craft CMS

- [Github Script](https://github.com/amezmo/craftcms-demo/blob/master/.amezmo/before.deploy)

## Drupal

- [Github Script](https://github.com/amezmo/drupal-demo/blob/master/.amezmo/after.pull)

For Drupal websites, you should use the [amezmo-drupal-integrations](https://github.com/sdubois/amezmo-drupal-integrations) Composer package.
