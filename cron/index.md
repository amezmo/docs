# Scheduled tasks with Cron

Use [Cron](https://man7.org/linux/man-pages/man8/cron.8.html)
as a way to schedule recurring tasks for your application.
When working with Cron, Amezmo manages the creation of the crontab file
that is required to execute your task, and the logging of the task output so you can
see the results in your Amezmo dashboard.
Crons are executed from your applications [current release](/docs/deployments/directories) directory.

## Schedules
A cron schedule represents when the task will be executed. You may use an alias for the following cron expressions.

<dl>
    <dt>@minutely</dt>
    <dd>Execute the task once every minute.</dd>
    <dt>@hourly</dt>
    <dd>Execute the task once every hour.</dd>
    <dt>@monthly</dt>
    <dd>Execute the task once every month.</dd>
    <dt>@weekly</dt>
    <dd>Execute the task once every week.</dd>
    <dt>@yearly</dt>
    <dd>Execute the task once every year.</dd>
</dl>

For advanced use cases,
Amezmo supports [POSIX cron syntax](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07).

## Scripts

A cron *script* is a bash script where you define your task logic. In this script, you may call into other
services such as PHP, Node.js and anything you'd normally do from the command line. Scripts run on your instance and in the current working
directory as your most recent [release](/docs/deployments/releases).

## Best practices
It's best to use a Cron job as a means to invoke another script. Don't put any logic into your Cron job. Keep your business logic in your [git](/docs/git) repository so that any updates won't require an update to your Cron job as well.

