# Nginx configuration

Your application has a default `nginx.conf` file that is generated dynamically based on your Nginx settings. To view all Nginx settings,
visit the Nginx tab within your Amezmo dashboard.

Amezmo generates and puts your Nginx configuration file at `/etc/nginx/nginx.conf` and
you may view the this file within your instance with the `cat` command line utility. 


## Customizing the Nginx configuration

For advanced applications, you may view and modify the default Nginx `location` directives that Amezmo generates for you. 
Amezmo supports adding and editing Nginx [location directives](https://nginx.org/en/docs/http/ngx_http_core_module.html#location).

