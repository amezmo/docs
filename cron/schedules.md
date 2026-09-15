# Cron Schedules

{.lead}
A cron schedule says when a [cron entry](index.md) runs: an alias such as
`@daily`, or a five-field POSIX cron expression.

## Aliases

Use an alias in place of its cron expression:

Alias              | Expression    | Runs
------------------ | ------------- | ---------------------------
`@minutely`        | `* * * * *`   | Every minute
`@every_5_minutes` | `*/5 * * * *` | Every five minutes
`@hourly`          | `0 * * * *`   | At the top of every hour
`@daily`           | `0 0 * * *`   | Every day at midnight
`@weekly`          | `0 0 * * 0`   | Every Sunday at midnight
`@monthly`         | `0 0 1 * *`   | On the first of every month
`@yearly`          | `0 0 1 1 *`   | On January 1
`@annually`        | `0 0 1 1 *`   | On January 1

`@yearly` and `@annually` resolve to the same expression, so pick either.
The dashboard's schedule dropdown offers the same aliases.

## Custom Expressions

When no alias fits,
Amezmo supports [POSIX cron syntax](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07).
See [custom cron expressions](custom-expressions.md) for the field order, the
operators, and the extensions to avoid.

## Schedules over the API

[Create a cron entry](../api/cron/create-cron-entry.md) and
[update a cron entry](../api/cron/update-cron-entry.md) take a schedule in
their `expression` parameter, as an alias or a five-field expression. The
response reports the resolved five-field `expression` along with the matching
`expression_alias`, so an alias you send comes out as both.
