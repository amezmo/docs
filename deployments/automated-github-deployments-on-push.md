# Automated GitHub Deployments on Push

With a GitHub repository connected, a push to your automatic deployment branch
starts a [deployment](index.md) with no action in the dashboard. This page
covers what happens between the push and the deployment, and why a push might
not deploy.

A push is one of two [deployment triggers](triggers.md). To start a deployment
yourself instead, see [manual deployments](manual-deployments.md).

## Set It Up

1. Connect GitHub from the Git tab of your environment. See
   [Git providers](../git/providers.md) for the difference between OAuth and
   the GitHub App.
2. Choose a repository and an
   [automatic deployment branch](../git/branches.md).
3. On the Deployments tab, under Deployment settings, keep Automatic
   deployments on.

Production and Staging each have their own repository settings, branch, and
Automatic deployments switch.

## What Happens When You Push

```bash
$ git push origin master
```

1. GitHub sends Amezmo a push event. With OAuth, the event comes from the
   webhook Amezmo created in your repository. With the GitHub App, it comes
   through the app installation.
2. Amezmo verifies the signature on the event and finds the environment
   connected to that repository.
3. Amezmo compares the pushed branch with the environment's automatic
   deployment branch.
4. On a match, Amezmo creates a deployment for the head commit of the push and
   queues it. The deployment shows up on the Deployments tab with the pusher's
   name and a link to the commit.

A push with several commits starts one deployment, for the newest commit.
Merging a pull request into the deployment branch counts as a push to that
branch, so it deploys too.

## Which Pushes Deploy

A push deploys only when its branch matches the environment's automatic
deployment branch. Pushes to other branches do nothing. If production and
staging use the same branch, one push deploys to both.

Two settings change the matching:

- Branch patterns. If you set ``auto_deploy_branch_patterns`` with the
  [Update an environment](../api/environments/update-environment.md) endpoint,
  Amezmo matches the pushed branch against those regular expressions and
  doesn't compare it with the fixed branch name.
- Tag patterns. Creating a tag deploys when the tag matches one of your
  [tag-based deployment](../git/tag-based-deployments.md) patterns.

Opening a pull request or publishing a GitHub release doesn't start a
deployment.

## When a Push Doesn't Deploy

If a push produces no deployment, check these first:

- Automatic deployments is off for that environment.
- The pushed branch isn't the automatic deployment branch. Remember that
  Production and Staging each have their own.
- The repository connection is incomplete or its authorization expired. See
  [Git troubleshooting](../git/troubleshooting.md).
- With OAuth, the webhook is missing from your repository or its deliveries
  fail. In GitHub, open the repository's Settings, then Webhooks, and look at
  the recent deliveries.

In two cases the deployment appears on the Deployments tab but doesn't run:

- Your plan's deployment allowance for the billing cycle is used up. The
  deployment gets an Ignored status.
- Your account has no payment method or is past due. The deployment gets a
  Payment required status.

## Turn Off Automatic Deployments

On the Deployments tab, under Deployment settings, switch off Automatic
deployments. Amezmo then ignores pushes for that environment, and you deploy
with [manual deployments](manual-deployments.md).

## Report Results Back to GitHub

For GitHub repositories, Deployment settings has two more switches. Both are
off by default.

Commit status checks
: Marks each deployed commit on GitHub with the result of its deployment.

GitHub deployments
: Records each deployment on GitHub, so it shows on pull requests and in your
  repository's Environments.
