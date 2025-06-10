# Password protection

By default, Amezmo doesn't configure your application to require a username/password to access
it over HTTP. However, you may enforce such restriction. When enabled, this setting
applies to all domains within your environment.

Implemented with Nginx's basic authentication module, you
may define a username and password combination that must be provided before accessing your application. Passwords
are hashed using the `crypt` algorithm and must be at least 8 characters.

Your application responds with [`401 Unauthorized`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401)
While HTTP Authentication is enabled and username and password combination doesn't match what you've defined.
