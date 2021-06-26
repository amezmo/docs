# PHP Caching

Caching dynamically generated PHP files can increase site speed by saving the result in a static file and serving it in subsequent requests.
PHP pages are cached by the unique URI associated with each page.

With caching enabled, dynamically generated PHP pages are cached at the edge and served as static files.
Caching makes applications significantly faster by reducing the amount of time and resources it takes to render a page.

To instruct Amezmo to cache your dynamically generated PHP pages, ensure the following requirements for each page you want to cache.

## Caching requirements

- Cookies disabled
Cookies, as in the `Set-Cookie` HTTP response header must not be present in any cachable page.
- Cache-Control
This HTTP response header must **not** be present
- Expires
This HTTP response header must **not** be present
- 2XX HTTP response code
Amezmo will only consider 200 level responses as candidates to be cached

It is important that sensitive pages such as admin portals and password reset forms are not cached.
By default `POST` requests are never cached.

**Important**: If you're using a PHP framework such as Laravel, or Yii, then cookies may be
automatically added to your HTTP responses.
You must disable this functionality before PHP caching will work.
To disable cookies, see the documentation for your framework.

## Helpful information
-  When a page is cached, the cached version will served for up to 24 hours.
    See ways of [purging the cache](/docs/caching/purging) for more information.
- Caching has an aggregate size limit of 256MB.
- Only `GET` requests are candidates for caching.

## Use cases

- **Marketing pages**
Your marketing pages are dynamically generated with a template engine such as
[Blade](https://laravel.com/docs/blade), or [Twig](https://twig.symfony.com/). These pages don't change often but each HTTP request must
call into PHP-FPM and run the PHP engine to generate the page. Caching these pages would make your marketing site behave as if it was a static HTML site instead.
- **WordPress**
Your blog posts probably don't change often, so there's no reason
to have PHP regenerate the page for each requests.


## See also

- [Purging cached pages](/docs/caching/purging)
- [URL Patterns](/docs/caching/patterns)
