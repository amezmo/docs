# after.deploy

The file after.deploy is executed after Amezmo updates your web server directory to the release directory.
The exit status of this script is ignored.

Because this hook will execute after your deployment has
[succeeded](/docs/deployments/directories#successful-deployments), it is not advised to use this
hook if there's a chance that the script will fail.

Relative to your application root directory, the
[full path](/docs/deployments/hooks#hook-files) of this hook is .amezmo/after.deploy.