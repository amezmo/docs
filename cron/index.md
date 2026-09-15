# Scheduled tasks with Cron

Use [Cron](https://man7.org/linux/man-pages/man8/cron.8.html)
as a way to schedule recurring tasks for your application.
When working with Cron, Amezmo manages the creation of the crontab file
that is required to execute your task, and the logging of the task output so you can
see the results in your Amezmo dashboard.
Crons are executed from your applications [current release](../deployments/directories.md) directory.

## In This Section

### Cron Schedules

An alias such as `@daily` or a five-field expression decides when an entry
runs. [Cron schedules](schedules.md) lists every alias with the expression it
resolves to, in the dashboard and over the API.

### Custom Cron Expressions

When no alias fits, write a five-field expression instead.
[Custom cron expressions](custom-expressions.md) covers the field order and the
operators, a table of ready-made schedules, and the syntax that saves but never
runs on your instance.

### Editing a Cron Entry

Change an entry's script or its schedule after you create it, from the dashboard
or the API. [Editing a cron entry](editing-entries.md) covers what you can change,
why the name is fixed, and when the change reaches your instance.

## Scripts

A cron *script* is a bash script where you define your task logic. In this script, you may call into other
services such as PHP, Node.js, and anything you'd normally do from the command line. Scripts run on your instance and in the current working
directory as your most recent [release](../deployments/releases.md).

## Best practices
It's best to use a Cron job as a means to invoke another script. Don't put any logic into your Cron job. Keep your business logic in your [git](../git/index.md) repository so that any updates won't require an update to your Cron job as well.

That pays off when a task changes: you deploy the new logic instead of
[editing the cron entry](editing-entries.md).

## API

The Amezmo API lists, gets, creates, and updates your cron entries. See
[Cron endpoints](../api/cron/index.md).
