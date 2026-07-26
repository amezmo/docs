# Nginx Configuration

Amezmo generates your ``nginx.conf`` from your Nginx settings and writes it to
``/etc/nginx/nginx.conf``. You can view it from your instance with ``cat``. Most
apps never need to touch it, because the defaults are tuned for PHP.

For finer control, edit the generated [location blocks](location-blocks.md), or
replace the whole file with your own.

## Full Custom Configuration

Advanced plans can replace the entire ``nginx.conf`` from the Nginx tab.
Amezmo saves your config, up to 1 MB, and applies it to your instance. It does
not check the config for syntax errors first, so a bad directive shows up only
after it applies. Watch the Nginx error log from the Log tab to debug.

If something goes wrong, restore the default config from the Nginx tab, which
drops your custom file and regenerates the default. Saving an empty config does
the same. You can also restart or stop Nginx from the Nginx tab.

## See Also

- [Location blocks](location-blocks.md)
- [Compression and caching](compression-and-caching.md)
- [HTTP authentication](http-authentication.md)
