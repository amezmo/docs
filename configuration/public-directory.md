# Public directory

Your applications public path is the entry point to your application. This is typically
the directory which has your `index.php` file. Other files such as assets, images, CSS, and JavaScript
files are server from this directory as well.
Amezmo provides a way to change your public path
from the dashboard. Go to your instance's Configuration tab to change this setting.

By default, Nginx will first check to see if a file exists in your public document root, and then
route all requests to an `index.php` file in the public document root that you've chosen.

## File uploads
Publicly accessible files can be served from your public document root.
By creating a symbolic link from a directory inside your public document root into the
`/webroot/storage/public` directory, you can perist file uploads across deployments.
[Learn more about persistent storage](/docs/configuration/storage).

Amezmo creates this directory for you at instance launch time and you are encouraged to use it as the persistent public
storage area for your app. Amezmo has tested a set of
[recommended file permissions](/docs/configuration/storage)


## Public directory symbolic link
The following deployment hook snippet has been tested and is the recommended way of setting up a persistent public storage
directory.

This file should be created in your repo at `.amezmo/after.pull`.

```bash
#!/bin/bash

# Make sure we fail our deployment if this hook fails.
set -e;

# More commands executed here.
# Please see https://www.amezmo.com/docs/deployments/dependencies
# for a full example

# APPLICATION_ROOT is a default variable provided at hook execution time
echo "Running this hook from ${APPLICATION_ROOT}";

# Create our symbolic link to point our public storage directory
# to our persistent storage directory
ln \
    --symbolic \
    --force \
    --no-dereference \
    /webroot/storage/public "${APPLICATION_ROOT}/public/storage";
```

## Resources
- [How to Persist Storage Across PHP Deployments on Amezmo Part 1](https://www.youtube.com/watch?v=A-iBIfch6Bw)
- [Laravel deployment hook for persistent storage](https://github.com/amezmo/demo.amezmo.com/blob/master/.amezmo/before.deploy)

