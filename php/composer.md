# Composer

Amezmo installs both Composer 1.x and Composer 2.x on every PHP instance.
Composer 1.x is the ``composer`` command, and Composer 2.x is the ``composer2``
command. Use either one in [deployment hooks](../deployments/hooks/index.md) or
over [SSH](../instances/ssh.md).

## The Default Version

New instances default to Composer 1, so ``composer`` runs version 1 until you
change the default. To switch an environment to Composer 2, open the Deployments
tab, then Settings, then the Composer packages settings, and choose version 2.
After that, automatic deployments use ``composer2``, and you don't need SSH to
make the change. See
[Change the default Composer version](../how-to-guides/change-default-composer-version.md).

## Composer on Deploy

When automatic Composer installs are on and your repo has a ``composer.json``,
each deployment runs ``composer install`` with the default version you chose,
then dumps an optimized autoloader. See
[Automatic Composer package management](../deployments/automatic-composer-installs.md).

## How-to Guides

- [Change the default Composer version](../how-to-guides/change-default-composer-version.md)
- [Enable or disable automatic Composer installs](../how-to-guides/disable-automatic-composer-installs.md)
