# after.extract

The after.extract hook is executed after Amezmo extracts the archive file provided with an [API deployment](../../api/deployments/index.md)

If your script returns a non-zero exit status,
the deployment fails. Relative to your application root directory, the
[full path](index.md#hook-files)
of this hook is `.amezmo/after.extract`

