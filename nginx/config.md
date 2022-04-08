# Nginx configuration

Your application has a default `nginx.conf` file that is generated dynamically based on your Nginx settings. To view all Nginx settings,
visit the Nginx tab within your Amezmo dashboard.

Amezmo generates and puts your Nginx configuration file at `/etc/nginx/nginx.conf` and
you may view the this file within your instance with the `cat` command line utility. 


## Customizing the Nginx configuration

For advanced applications, you may view and modify the default Nginx `location` directives that Amezmo generates for you. 
Amezmo supports adding and editing Nginx [location directives](https://nginx.org/en/docs/http/ngx_http_core_module.html#location).


## Nginx location directives
Nginx `location` directives are related to your environment. These directives are automatically created for you, and they're based on the application type that
you choose in the Git repository wizard. You may see your app type by going to the Git tab within your Amezmo dashboard. Because the directives are generated 
based on the application type, changing your application type will reset the Nginx location directives to the Amezmo default set. 

The Drupal application type is the only application type that has a specialized set of configurations for Nginx. Laravel, Craft CMS, WordPress, and standard PHP 
applications all use the same configuration set. 

## Editing locations
You may edit, delete, and add new Nginx location blocks for your PHP application. By default, Amezmo generates a set of rules for your based on your application type. To help with debugging custom location blocks, you may look at the Nginx error log from the Log tab.
