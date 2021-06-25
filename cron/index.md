# Scheduled tasks with Cron

Use [Cron jobs](https://stackoverflow.com/questions/21615673/difference-between-cron-crontab-and-cronjob)
as a way to schedule recurring tasks for your application. When working with Cron, Amezmo manages the
creation of the crontab file that is required to execute your task, and the logging of the task output so you can
see the results in your Amezmo dashboard. Crons are executed from your applications [current release](/docs/deployments/directories) directory.

## Schedules
A cron schedule represents when the task will be executed. Amezmo provides a simple representation of
the complex and often times confusing cron expression syntax.

- @minutely &mdash; Execute the task once every minute
- @yearly &mdash; Execute the task once every year
- @monthly &mdash; Execute the task once every month
- @weekly &mdash; Execute the task once every week
- @hourly &mdash; Execute the task once every hour

## Scripts

A cron *script* is a bash script where you define your task logic. In this script, you may call into other
services such as PHP, Node.js and anything you'd normally do from the command line.

