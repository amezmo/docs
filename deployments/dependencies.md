# Installing Composer/NPM dependencies

Hooks on Amezmo
are simply bash script files located in the top level `.amezmo` directory.
Use the [.amezmo/after.pull](/docs/deployments/hooks/after-pull) hook to install Composer dependencies.
Be sure to commit your `composer.lock` files to source control in order to speed up package installation.

Your application directory should have the `.amezmo` directory created as shown below.

```bash
# This is your application directory structure.
.
├── .amezmo
│   ├── after.pull
├── app
├── storage
├── public
├── .env
```

```bash
#!/bin/bash

# Path to this script: &lt;your repo&gt;/.amezmo/after.pull
#
# IMPORTANT: set -e is required to instruct Bash to
# exit if any command
# returns a non-zero exit code
set -e;

# RELEASE_ID is a predefined variable that
# Amezmo sets upon executing this script
echo "Running script after.pull for release ${RELEASE_ID}";

composer \
    --no-ansi \
    --no-interaction \
    --optimize-autoloader \
    --no-progress \
    --no-dev \
    --profile \
    install

# Uncomment if using Laravel
# php artisan migrate --no-interaction --no-ansi --force;

# NOTE:
# The following command has been tested and strongly recommended
# for fast deployments Amezmo will persist
# node_modules to /webroot/node_modules and symbolically
# link /webroot/release/$RELEASE_ID to /webroot/node_modules
# directory so a fresh install
# is not required for each deployment

if [ -f "package.json" ]; then
    NODE_ENV=production npm \
        --no-audit \
        --no-optional \
        --only=prod \
        --no-progress install;
fi
```

Composer and NPM are setup for you out of the box when you launch an instance.
If you're not commiting your vendor or node_modules directory to source control, then you can install your dependencies
with a deployment hook.

To make deployments fast and to not require a fresh install of Composer/NPM packages for each deployment,
Amezmo has implemented a persistency pattern so your deployments execute fast.

Amezmo will persist a reference to your
`node_modules` directory at `/webroot/node_modules` and symbolically
link `/webroot/release/$RELEASE_ID` to your `/webroot/node_modules`
directory so a fresh install
is not required for each deployment.

## Using Hooks to Install Dependencies
[Deployment hooks](/docs/deployments/hooks) are files defined under the `.amezmo`
directory inside your root directory of your application. You must create
this directory and create deployment scripts inside this directory.

It's important that your script runs in non-interactive mode in order to prevent your deployment from failing.
Deployment hooks currerntly have an execution [limit](/docs/deployments/hooks#limits).
We recommend using the following script for installing dependencies with Composer. See below for a working deployment hook example.

## Resources
- [Example project](https://github.com/amezmo/demo.amezmo.com) provides advanced examples of deployment hooks