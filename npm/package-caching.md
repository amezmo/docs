# NPM Package caching

Package caching is enabled by default. This allows you to not have to build a fresh `node_modules`
directory for each deployment. By caching packages, it's likely your deployments will be significantly faster.
Amezmo implements this by creating a symbolic link from your [release directory](../deployments/directories.md)
to your [environment root directory](../environments/environment-directory.md)

## How-to Guides

- [How to turn off package caching](../how-to-guides/turn-off-npm-package-caching.md)