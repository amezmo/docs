# PHP Caching patterns

Amezmo caches your PHP script output based on a set of caching patterns that you must provided from the settings tab
under Caching. See below for sample caching URL patterns.

Caching conditions operate on the Request-URI, not the URL. For example, if our domain is `example.com`,
Caching URI patterns target everything after the `.com`

The examples below are regular expression based an exact match. Matching happens per repository/environment
and for all the domains associated with it.

## URI patterns
- **Cache everything**
`.*`
- **Per page**
`/pricing`


## Helpful tips

- Rules are **case-sensitive** meaning, for example, `wp-admin/*` is not the same as `WP-admin/*`.


## See also
- [PHP Caching Overview](/docs/caching)
- [Purging cached pages](/docs/caching/purging)