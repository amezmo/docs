# Git repositories on Amezmo

All deployments on Amezmo are made with a Git repository. Often times, a `git push` will trigger 
an [automated deployment](/docs/deployments).

Application instances on Amezmo, are associated with a Git repository after 
connecting one from your chosen Git provider.
You may associate a repository from GitHub, BitBucket, or GitLab with the Git wizard. Additionally, 
automatic deployments are started when commits are made to the [automatic deployment branch](/docs/git/branches).

## Git providers
Amezmo supports the following Git integrations: 

- GitHub 
- BitBucket
- GitLab

## Branches
Upon importing a repository, you must first choose an automatic deployment deployment branch. 
With automatic deployments enabled, commits to this branch will trigger a new deployment each time. The automatic deployment branch
may be changed at anytime. To learn more about this see the Git tab.

