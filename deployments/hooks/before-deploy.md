# before.deploy

Amezmo runs `before.deploy` before it updates your web server directory. If your
script returns a non-zero exit status, the deployment fails.

Relative to your application root directory, the
[full path](index.md#hook-files)
of this hook is `.amezmo/before.deploy`.

A common use is linking a
[persistent storage directory](../../how-to-guides/setting-up-the-storage-directory.md)
into each release.
