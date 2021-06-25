# before.pull

The file before.pull is executed before Amezmo fetches the latest updates from your git provider.
The exit status of this script is ignored. Relative to your application root directory,
the [full path](/docs/deployments/hooks#hook-files)
of this hook is .amezmo/before.pull.

## Remarks
It's not possible to run the `before.pull`
if you've never had at least one [successful deployment](/docs/deployments/directories#successful-deployments) that has had the `.amezmo/before.pull` file (hook) present.
This hook runs with the [current release](/docs/deployments/releases) and it is impossible to run the before.pull file before actually
pulling the contents of the repository for the first time.

This hooks always runs with the *current* release version of the .amezmo/before.pull file. So if you've updated before.pull
and then pushed, the file that will be executed will be the previous version, not the most recent version. The version that is executed upon
deployment is always one version behind the most recent version.
