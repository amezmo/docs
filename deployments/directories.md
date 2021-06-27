# Deployment Directories

For each deployment, Amezmo creates a new directory under `/webroot/release`. This contents of this directory 
are effectively the results of running `git pull` at the time the deployment was executed.

If the deployment succeeds, Amezmo updates the `/webroot/current` symbolic link to point to the
new deployment directory that was created.

```bash
/webroot/release/${TIMESTAMP}.${COMMIT_ID}
```

## Directories

The timestamp variable above is in the form of `YYYY-MM-DDTHH:MM:SS.mmmmmm`, and the commit ID is
short form version of the SHA1 Git commit hash.

Amezmo maintains an [environment directory](/docs/environments/environment-directory) per environment
inside your instance to implement atomic deployments and to separate staging and production.
Throughout this documentation,
we refer to the "current release directory" as the directory that was created as a result of a succesfull deployment.

```bash
/webroot
    |----logs
    |----storage
    |----node_modules
    |----vendor
    |----current -> /webroot/release/${TIMESTAMP}.${COMMIT_ID}
    |----release
    |-------${TIMESTAMP}.${COMMIT_ID}
    |-------${TIMESTAMP}.${COMMIT_ID}
```

## Successful deployments

All of the following conditions must be met for a deployment to be considered successful

- The git repository and branch exists and is visible from Amezmo
-  No non-zero exit status codes from any of your hooks. However, the exit statuses of the following hooks will not affect the deployment outcome.
    - [before.pull](/docs/deployments/hooks/before-pull)
    - [after.deploy](/docs/deployments/hooks/after-deploy)
    - [deploy.success](/docs/deployments/deploy-success)

As a final step in the deployment process, the symbolic link located at `/webroot/current`
is atomically updated to point the new release directory.

As part of the deployment process, Amezmo will run a chmod across your target deployment directory. This ensures that
any files created from your hooks will have correct and expected permissions. Amezmo ensures the owner/group is
`www-data:deployer`. This allows for expected permissions across all areas of your application.

For directories, the permissions are `2775/drwxrwxr-x`, for files the permissions are `0664/-rw-rw--r--`.

## Failed deployments
For a deployment to enter the Failed state, any of the following conditions must be met:

- Amezmo cannot validate the git repository or branch
- Any hook, except for <a href="/docs/deployments/hooks/before-pull">before.pull</a>,
        <a href="/docs/deployments/hooks/after-deploy">after.deploy</a>, and
        <a href="/docs/deployments/hooks/deploy-success">deploy.success</a>
        exits with a non-zero status.

When a deployment step fails, the process will be aborted. This means that your 
**current release will not be   affected** by a failed deployment, as Amezmo only updates your symbolic link as a final step in the process.


