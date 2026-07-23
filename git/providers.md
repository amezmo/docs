# Git Providers

Amezmo is a Git-native deployment platform. You can deploy from GitHub, GitLab,
and Bitbucket.

You connect a provider from the Git tab. Amezmo asks you to authorize with the
provider, stores an access token for that account and uses it to list your
repositories, add a deploy key and create a webhook for automatic deployments.

## Permissions Amezmo Needs

To add the deploy key and webhook, the account you authorize with needs admin
rights on the repository. If you authorize with an account that can't administer
the repo, the connection fails with a 403. See
[Git troubleshooting](troubleshooting.md).

## GitHub: OAuth or the GitHub App

GitHub gives you two ways to connect:

- Standard OAuth authorizes your GitHub account.
- The GitHub App, shown as advanced authentication, installs Amezmo on the
  repositories you pick. This suits organizations that grant access one repo
  at a time. With the app, authorizing isn't enough: you also install it on the
  repository you want to deploy.

GitLab and Bitbucket connect through standard OAuth.

## See Also

- [Git troubleshooting](troubleshooting.md)
- [Repos](repos.md)
- [Branches](branches.md)
- [Deployment triggers](../deployments/triggers.md)
