# Compression and Caching

The Nginx tab has two switches that speed up how your site serves assets.

## Gzip Compression

Turn on Gzip to compress text assets like JavaScript, CSS and HTML before Nginx
sends them, which cuts download size. Amezmo supports Gzip. There's no Brotli
option.

## Static File Caching

Turn on static file caching to serve static files (``js``, ``css``, ``png``,
``jpg``, ``jpeg``, ``gif``, ``ico``, ``ogv``) straight from disk, skipping PHP.
Cached files return a ``304 Not Modified`` when the browser already has them,
which saves bandwidth.

## See Also

- [Nginx configuration](config.md)
