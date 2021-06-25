# after.pull

The hook after.pull is executed after Amezmo fetches the latest updates from your git provider.
This script is where you would want to
[fetch dependencies from Composer](/docs/deployments/dependencies)


If your script returns a non-zero exit status,
the deployment fails. Relative to your application root directory, the
[full path](/docs/deployments/hooks#hook-files)
of this hook is `.amezmo/after.pull`

