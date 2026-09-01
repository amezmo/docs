# Deployments with Git

Amezmo is a Git-first deployment platform that supports GitHub, GitLab and
BitBucket, with automatic deployments and a set of
[deployment hooks](../deployments/hooks/index.md). Each time you push, Amezmo
starts a new deployment. You can also turn off automatic deployments and deploy
the branches you choose.

## In This Section

### Branches

A deployment starts from a repository and the branch you choose for automatic
deployment. [Branches](branches.md) covers picking and changing it.

### Git Providers

[Connect GitHub, GitLab, or Bitbucket](providers.md) from the Git tab. Amezmo
stores an access token for that account and uses it to list your repositories.

### Repos

Every deployment runs from a [Git repository](repos.md) attached to your
instance once you have connected a provider.

### Tag-Based Deployments

Deploy from [tags matching a regular expression](tag-based-deployments.md)
instead of a fixed branch name.

### Troubleshooting

[Git troubleshooting](troubleshooting.md) covers the problems you can hit
partway through connecting a provider, choosing a repository, or adding a deploy
key.

## Automation

Read more about [installing Composer packages and running migrations
automatically](../deployments/automatic-composer-installs.md), without a custom
script.
