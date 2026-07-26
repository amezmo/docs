# Git Troubleshooting

Amezmo connects to your Git provider through a short wizard on the Git tab:
choose a provider, authorize, choose a repository, add a deploy key, then
finish. See [Git providers](providers.md) for how connecting works. This page
covers the problems you might hit along the way.

## When Continue Doesn't Work

The Continue button sends you to your provider with a full-page redirect, not a
popup, so a popup blocker isn't the cause. A script or ad blocker, blocked
third-party cookies or an idle tab that lost its session can interrupt it.

If you return to a message like "GitHub authorization has expired. Please go
back and try again," your browser dropped the session between leaving and coming
back. Go back, reload the Git tab and click Continue again in the same browser,
with cookies allowed for amezmo.com.

## A Deploy Fails with 403 from the Provider

A 403 means your provider refused the request. The usual causes:

- The authorizing account can't administer the repository. Adding a deploy key
  and a webhook needs admin rights, so authorize with an account that has them.
- The repository is private and the connected account can't see it. Reconnect
  with an account that has access.
- On the GitHub App flow, you authorized the app but never installed it on the
  repository. Install the Amezmo app on that repo, then try again.
- The deploy key isn't on the repository yet. Add it in the Add deploy key step.

Bitbucket passes its own reason through, shown as "BitBucket said: ...". Read
that message, fix what it names (usually access or scope), then authorize again.

## Your Authorization Expired

Provider tokens expire, and GitLab and Bitbucket tokens are short-lived. When a
token expires or you revoke it, Amezmo marks the repository as needing
authorization. Reset the authorization token (below) and click Continue to
reconnect.

## Recovering

Each action below lives on the Git tab. Use the smallest one that fits:

- Reset the authorization token keeps your repository choice and deploy key and
  clears the stored provider token. Use it after a token expires.
- Reset the repository keeps the provider connection, clears your repository
  choice and generates a fresh deploy key. Use it to pick a different repo or to
  get a new deploy key.
- Start over clears the provider, authorization, repository and deploy key, then
  restarts the wizard from the first step.

If a deploy reports "To deploy, please complete the Git wizard," the wizard
isn't finished. Reopen the Git tab and complete every step.

## Deploy Keys

Amezmo uses one SSH deploy key per repository for read access to your code. The
Add deploy key step shows the public key and links to the page where you add it
at your provider:

- GitHub: Settings, then Deploy keys
- GitLab: Settings, then CI/CD, then Deploy keys
- Bitbucket: Repository settings, then Access keys

Add the key, then continue the wizard. To replace a key, reset the repository to
generate a new one, then add the new key at your provider.
