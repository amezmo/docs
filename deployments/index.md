# Deployments


Amezmo implements atomic, real-time deployments based on your `git push` activity. When your repo
has new push events, Amezmo will be notified and immediately begin a deployment process.

## Configuration files

An `.env`, will be placed into your root
[deployment directory](/docs/deployments/directories) automatically. This will overwrite
any existing `.env` file your archive may have.

## Deployment directories
The deployment directory section describes the layout for zero-downtime deployments
[Learn more](/docs/deployments/directories).

## Hooks
Amezmo's extensibible deployment systems provides you the capability to run your own code at
any step of the deployment process. [Learn more](/docs/deployments/hooks).

## Releases
After a successful deployment, then the deployment is considered a release. You may rollback to a previous
release at anytime. [Learn more](/docs/deployments/releases).

## Fault tolerance
Your application will not be affected by a failed deployment, as Amezmo only releases your successful deployments.
