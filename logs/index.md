# Logs

The Logs tab shows two kinds: your application logs and your server logs.

## Application Logs

Your application logs are the files your app writes to ``/webroot/logs``. Amezmo
lists them on the Logs tab. To set your framework up to write there, see
[Logging](../configuration/logging.md).

## Server Logs

Amezmo also surfaces the server logs for your stack:

- Nginx error log
- PHP-FPM log
- MySQL error log, if your instance runs MySQL

Which logs appear depends on what your instance runs.

## Viewing a Log

Open a log from the Logs tab to see its most recent lines. The viewer shows a
tail of the file, not the whole thing, so a large log is truncated. To read a
log in full, download it.

## Downloading a Log

Download a log from its menu on the Logs tab. Amezmo prepares the file and gives
you a short-lived link to save it. You download one file at a time.

## Exporting

To send logs to your own S3 bucket, once or on a schedule, see
[Exporting logs](exporting.md).
