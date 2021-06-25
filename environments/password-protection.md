# Password-protection

By default, Amezmo doesn't configure your application to require a username/password to access
it over HTTP. However, you may enforce such restriction. When enabled, this setting
applies to all domains within your environment.

Implemented with Nginx's basic authentication module, you
may define a username and password combination that must be provided before accessing your application. Passwords
are hashed using the `crypt` algorithm and must be at least 8 characters.

While HTTP Authentication is enabled and username/password combination doesn't match what you've defined,
your application will respond with 401 (Authorization Required).

