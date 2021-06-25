# NPM Package caching

Package caching is enabled by default. This allows you to not have to build a fresh `node_modules`
directory for each deployment. By caching packages, it's likely your deployments will be significantly faster.
Amezmo implements this by creating a symbolic link from your [release directory](/docs/deployments/directories)
to your [environment root directory](/docs/environments/environment-directory)

## How-to Guides

- [How to turn off package caching](/docs/how-to-guides/turn-off-npm-package-caching)