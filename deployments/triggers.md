# Deployment Triggers

In this section, you will learn about how your
[PHP deployments](index.md) can begin for your sites.

## PHP Deployment Mechanisms
Atomic PHP deployments take place from an automatic process by which
your [instance](../instances/index.md) is aware of changes you make to
your [git repository](../git/repos.md). Amezmo creates a webhook
in your repository using your selected [integration](../git/providers.md).

## Deployment Scenarios

A deployment starts in one of two ways:

- A push to your automatic deployment branch. See
  [Automated GitHub deployments on push](automated-github-deployments-on-push.md)
  for what happens between the push and the deployment.
- A click on Deploy now in the dashboard. See
  [manual deployments](manual-deployments.md) for deploying any branch on
  demand.
