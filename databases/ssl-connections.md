# Remote SSL Connections to MySQL

You can enable access to your MySQL database securely with SSL. You're required to
provide a set of trusted IP addresses before your MySQL server will be exposed to the Internet.
Only SSL connections are permitted.

## Trusted sources for remote MySQL connections
Add your trusted sources from the Database > Security tab. After providing your IP addresses,
you can download your certificate files which you'll use to connect securely to your database server.

SSL certificate files are unique to the instance. These files do not change and are persistent until
the instance is terminated. Adding or removing trusted IP addresses won't change the certificate.

## SSL Certificate Files
Get your SSL certificate files by going to Database Settings.

<img alt="Image of Database > Settings" src="/assets/cert-files.png" class="img-fluid" />

## Resources
-  <span class="badge bg-info">Video</span> [How to Connect to MySQL remotely with SSL](https://www.youtube.com/watch?v=EyRZ-fjLxIA)
- [Laravel Configuration for MySQL Connections over SSL](https://github.com/amezmo/demo.amezmo.com/blob/master/config/database.php#L61)