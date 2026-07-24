# Exporting Logs

You can export your logs to your own Amazon S3 bucket, either one file at a time
or on a recurring schedule. Exporting works on any plan, once you add four
secrets.

## Set the S3 Secrets

Exporting reads your S3 credentials from [secrets](../secrets/index.md). In
Configuration, then Secrets, add these four:

- ``S3_LOG_EXPORT_BUCKET``
- ``S3_LOG_EXPORT_REGION``
- ``S3_LOG_EXPORT_ACCESS_KEY``
- ``S3_LOG_EXPORT_SECRET_KEY``

Until all four exist, an export fails with a message like this:

> Could not export: Missing secrets S3_LOG_EXPORT_REGION,
> S3_LOG_EXPORT_SECRET_KEY, S3_LOG_EXPORT_ACCESS_KEY, and S3_LOG_EXPORT_BUCKET.
> Go to Configuration > Secrets to create them.

Secrets take effect on your next deployment, so deploy once after you add them.

## Export a Log Now

From the Logs tab, choose Export to S3 on a log to send it to your bucket.
You can also select several logs and export them together.

## Export on a Schedule

Turn on scheduled exports to send your logs to S3 automatically. You provide a
[cron expression](../cron/index.md) for how often it runs. Each instance has one
export schedule.

## See Also

- [Logs](index.md)
