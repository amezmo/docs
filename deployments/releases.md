# Releases

After a [successful deployment](/docs/deployments/directories#successful-deployments), the deployment is considerd a release.
A release is promoted to the current release if the deployment has succeeded.

## Rollbacks
Amezmo defines a release "Rollback" as changing the active release to a previous release. Rolling back
your current release to a previous release does not trigger a new deployment. A rollback is an atomic operation.
Your web application will begin serving files from your previous release immediately. Your workers are also
reloaded after your symbolc link is updated. See below for the list of hooks Amezmo will look for when you execute
a rollback operation.


## Hooks
Upon rolling back your current release, Amezmo will execute the following scripts:

| Hook | Description
-------|-------------
.amezmo/rollback/before | This script is executed before Amezmo updates your [current release directory](/docs/deployments/directories) (Live)
.amezmo/rollback/after | his script is executed after the symbolic link directory is updated.

<p class="alert alert-info">
    Note: The scripts that are executed are the scripts defined in your **current** release. This means that
    when you execute a rollback, the scripts that will run are the ones that exist in your current release directory,
    not the target rollback.
</p>