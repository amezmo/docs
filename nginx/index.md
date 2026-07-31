# Nginx

{.lead}
**Nginx** runs in front of every application on Amezmo and serves it in
production from the first deploy. It terminates TLS, serves static files
directly from your public document root and passes dynamic requests to
PHP-FPM. You adjust the parts that vary per application through the pages below.

- [Configuration](config.md) documents the directives Amezmo generates and the
  values you can override.
- [Location blocks](location-blocks.md) route requests and add rules for
  specific paths in your application.
- [Compression and caching](compression-and-caching.md) sets response
  compression and cache headers for static assets.
- [HTTP authentication](http-authentication.md) puts a username and password in
  front of a site or a path.
