# before.deploy

The file before.deploy is executed before Amezmo updates your web server directory.
If your script returns a non-zero exit status, the deployment fails.

Relative to your application root directory, the
[full path](/docs/deployments/hooks#hook-files)
of this hook is `.amezmo/before.deploy`

