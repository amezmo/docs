# Nginx Password-protected applications

Password protection for sites is implemented using basic HTTP authentication. Enabling authentication on
an [environment](/docs/environments) applies to all domains that are associated with the environment in which you enable authentication on.

Upon editing the users for your password-protected environment, a job is submitted to test and reload your [Nginx configuration](/docs/nginx/config). 