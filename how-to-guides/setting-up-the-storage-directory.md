# Setting up the storage directory

{.lead}
The **persistent storage directory** holds files that must survive deployments,
such as user uploads. Each deployment creates a new release directory, so files
written inside a release are lost on the next deploy. Amezmo keeps
`/webroot/storage` outside the release tree and links it into each deployment,
so its contents persist. See [persistent storage](../configuration/storage.md)
for the directory layout.

You link the storage directory into your application from a
[before.deploy](../deployments/hooks/before-deploy.md) hook, which Amezmo runs
before it swaps in the new release. The scripts below link your framework's
storage path to `/webroot/storage`.

## Laravel

The demo application includes a `before.deploy` script that links the Laravel
storage directory to the persistent directory:

- [before.deploy for Laravel](https://github.com/amezmo/demo.amezmo.com/blob/master/.amezmo/before.deploy)

## Craft CMS

The Craft CMS demo application includes an equivalent script:

- [before.deploy for Craft CMS](https://github.com/amezmo/craftcms-demo/blob/master/.amezmo/before.deploy)

## Drupal

Drupal links its files directory after the code is pulled, so it uses an
[after.pull](../deployments/hooks/after-pull.md) hook:

- [after.pull for Drupal](https://github.com/amezmo/drupal-demo/blob/master/.amezmo/after.pull)

Drupal sites also use the
[amezmo-drupal-integrations](https://github.com/sdubois/amezmo-drupal-integrations)
Composer package.
