# Post deployment health checks

Upon a [successful deployment](/docs/deployments/directories#successful-deployments), you may
choose to have Amezmo run a post-deployment health check to your desired endpoint. The post-deployment healthcheck
attempts to make an HTTP request to your specified endpoint and checks the HTTP response status. If the response status
is not 200, then the post deployment health check will fail and you will be notified via email.

The post-deployment health check runs after a deployment meets the critera to be considered a successful deployment
and after the <a href="/docs/deployments/directories">deployment release directory</a> has been promoted to the current release.

If any problems with your
deployment was not detected by a [deployment hook](/docs/deployments/hooks),
then Amezmo would not have known that your deployment should be considered a failure. Post-deployment health checks
solve the problem of ensuring your application remains stable. By using a post-deployment health check, you can
be notified immediately of any problems.


## Rolling back a release

If you'd like to rollback a release after your post-deployment health check has failed, then you may
manually execute the rollback from the Deployments tab in your Amezmo dashboard. You may also
configure your deployments to automatically rollback to the most previous release upon a post-deployment
health check failing. Automatic rollbacks instruct Amezmo to automatically change your current release to the most
recent release.
