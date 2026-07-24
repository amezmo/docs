# Nginx Location Blocks

A location block is an Nginx ``location`` directive scoped to your app. Amezmo
generates a default set based on your app type (Laravel, Craft, WordPress,
Drupal or plain PHP), and you can edit them or add your own from the Nginx tab.

## Editing a Block

You can edit the body of a block, add a block or delete one. The ``location``
line itself is fixed, so to change the match you delete the block and add a new
one. When you add a block, put the body on its own line after the opening ``{``.

Changing your app type in the Git wizard resets the generated blocks to the
defaults for the new type, and leaves your custom blocks alone. To debug a
block, read the Nginx error log from the Log tab.

## Proxying to a Local Port

If you run a process on your instance, such as a Node app on port 3000, you can
proxy requests to it with a location block. Add ``proxy_pass`` with the local
address, plus the headers a proxied app needs. For WebSockets, add the upgrade
headers:

```nginx
# nginx location block: proxy to a local Node process
location /app {
    proxy_http_version 1.1;
    proxy_set_header Host $http_host;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_pass http://127.0.0.1:3000;
}
```

To route a whole domain to a worker process instead, see
[domain routing](../domains/routing.md), and to mark a path for WebSockets, see
[domain rules](../domains/rules.md).

## Coming from .htaccess

Amezmo runs Nginx, not Apache, so it ignores ``.htaccess`` files. Move your
rewrite, redirect, deny and expires rules into location blocks or your custom
[Nginx configuration](config.md). For password protection, use
[HTTP authentication](http-authentication.md).
