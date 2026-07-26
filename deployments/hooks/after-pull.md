# after.pull

The hook after.pull is executed after Amezmo fetches the latest updates from your git provider.
This script is where you would want to
[fetch dependencies from Composer](../dependencies.md)


If your script returns a non-zero exit status,
the deployment fails. Relative to your application root directory, the
[full path](index.md#hook-files)
of this hook is `.amezmo/after.pull`

