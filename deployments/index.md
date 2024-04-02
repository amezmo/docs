# Deployments

Amezmo implements atomic, real-time deployments based on your `git push`
activity. When your repo has new push events, Amezmo will be notified and
immediately begin a deployment process.

You can use Amezmo to ensure your PHP application is highly available. Deployments
on Amezmo combine a series of atomic steps that operate in a pipeline. Pipeline
steps have success conditions. Conditions are checked as a prerequisite for
advancing to the next step in the pipeline. In the case of a negative
success condition evaluation, your deployment pipeline safely terminates leaving
your active, or live site unaffected.

## Deployment pipeline success critera

You can keep your production site highly available to your users or
customers with Amezmo Atomic Deployments&mark. Amezmo deploys your
PHP application with a pipeline Atomicity. This gurantees invariability between
your live production site, and a failed deployment. There's no risk in
automating your [PHP deployments](/docs/git).

Amezmo deploys your PHP application to production in a pipeline comprised of
indivisible units of well-defined deployment tasks.

## Configuration files

An `.env`, will be placed into your root
[deployment directory](/docs/deployments/directories) automatically. This will overwrite
any existing `.env` file your archive may have.

## Deployment directories

The deployment directory section describes the layout for zero-downtime deployments
[Learn more](/docs/deployments/directories).

## Hooks

Amezmo's extensible deployment systems provides you the capability to run your own code at
any step of the deployment process. [Learn more](/docs/deployments/hooks).

## Releases

After a successful deployment, then the deployment is considered a release. You may rollback to a previous
release at anytime. [Learn more](/docs/deployments/releases).

## Fault tolerance

Your application will not be affected by a failed deployment, as Amezmo only releases your successful deployments.
