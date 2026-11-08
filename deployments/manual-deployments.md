# Manual Deployments

A manual deployment starts when you click Deploy now in the dashboard, not when
you push to your repository. It runs the same [deployment pipeline](index.md)
as an automatic deployment, with the same
[hooks](hooks/index.md) and the same zero-downtime switch to the new release.
Only the [trigger](triggers.md) differs.

## When to Deploy Manually

- You turned off automatic deployments and want to choose when each release
  goes out.
- You want to deploy a branch other than the
  [automatic deployment branch](../git/branches.md), such as a hotfix branch on
  staging.
- You connected a repository and want its first deployment without pushing a
  new commit.
- A deployment failed for a reason outside your code, and you want to run it
  again.

On GitHub, a push can start the deployment for you. See
[Automated GitHub deployments on push](automated-github-deployments-on-push.md).

## Start a Manual Deployment

Your environment needs a connected repository. Until you finish the Git wizard,
the Deployments tab shows Setup git now in place of Deploy now.

1. Open your instance in the Amezmo dashboard.
2. Select the Production or Staging tab.
3. Open the Deployments tab.
4. Click Deploy now.
5. Choose a branch. The automatic deployment branch is selected by default.
6. Click Start deployment.

The new deployment appears at the top of the Deployments list with a Pending
status, and the list updates as the deployment runs.

## What Gets Deployed

A manual deployment deploys the latest commit on the branch you choose. You
can't pick an older commit or a tag. To go back to earlier code, roll back to a
previous [release](releases.md).

The confirmation modal shows the short hash of the commit it will deploy. For a
GitHub repository it also links to View changed files, which compares that
commit with your current release.

Choosing a different branch affects this deployment only. Your automatic
deployment branch stays the same, so the next push to it deploys as usual.

## Limits

An instance runs up to five deployments at a time. When five are active, wait
for one to finish before you start another.

Manual deployments count toward your plan's deployment allowance for the billing
cycle. When the allowance is used up, Amezmo records the deployment with an
Ignored status and doesn't run it.

## Deploying Without Git

To deploy from a build pipeline without a Git provider, upload an archive with
the [Create a deployment](../api/deployments/post.md) API endpoint.
