# Git Branches

[Deployments](../deployments/index.md) on Amezmo begin with a
[Git repository](repos.md) and a branch chosen for automatic deployment.

## The Automatic Deployment Branch

The automatic deployment branch is the branch that triggers a new
[deployment](../deployments/index.md) when you push commits to it. You choose
this branch when you import the repository, and you can change it at any time.

Instead of a fixed branch, you can also deploy from matching
[Git tags](tag-based-deployments.md).

## A Branch per Environment

Staging and production are separate environments, and each one has its own
automatic deployment branch. A push deploys to an environment only when the
pushed branch matches that environment's branch, so the two environments deploy
independently.

This is why a push to ``develop`` can deploy to both staging and production: it
happens when production's deployment branch is also set to ``develop``. To make
production deploy only from ``master``, set the production environment's branch
to ``master`` and leave staging on ``develop``.

To change the branch for one environment, select the Production or Staging tab
first, then change the repository from the Git tab. For the full steps, see
[Changing the automatic deployment branch](../how-to-guides/change-automatic-deployment-branch.md).

## See Also

- [Git providers](providers.md)
- [Changing the automatic deployment branch](../how-to-guides/change-automatic-deployment-branch.md)
- [Tag-based deployments](tag-based-deployments.md)
