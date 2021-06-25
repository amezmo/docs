# after.extract

The after.extract hook is executed after Amezmo extracts the archive file provided with an [API deployment](/docs/api/deployments)

If your script returns a non-zero exit status,
the deployment fails. Relative to your application root directory, the
[full path](/docs/deployments/hooks#hook-files)
of this hook is `.amezmo/after.extract`

