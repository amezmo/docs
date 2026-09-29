# Creating a cron entry

{.lead}
Create a [cron entry](index.md) from the dashboard: name it, pick a schedule,
and write the bash script it runs.

## Creating from the dashboard

Open your instance, go to **Cron**, and click **New**. Fill in the name, the
schedule, and the script, then click **Save**.

An entry belongs to the environment you have selected when you create it, so
switch to staging first if that is where the task should run. To run the same
task in both, create an entry in each. Your instance also has to be running: an
instance that is paused or still provisioning rejects the change.

## Name

The name identifies the entry in the cron list and decides the name of its
[log file](viewing-logs.md). It takes letters, numbers, and hyphens, starts with
a letter or a number, and is at most 63 characters, so spaces, dots, and
underscores are out. It has to be unique among the entries in its environment.
Reuse one and the form answers `Another entry already exists with this name.`

Choose it deliberately, because the name is permanent.
[Editing a cron entry](editing-entries.md) covers why, and what to do when you
need a different one.

The form prefills the fields to match your application where it recognizes the
framework:

Application | Name                      | Schedule    | Script
----------- | ------------------------- | ----------- | -----------------------
Laravel     | `Laravel-task-scheduler`  | `* * * * *` | `php artisan schedule:run`
Craft CMS   | `Craft-CMS-queue-runner`  | `* * * * *` | `php craft queue/run`
Drupal      | `Cache-clear`             | `0 0 * * *` | `drush cr`

Anything else starts with an empty name, `* * * * *`, and a bare
`#!/bin/bash` script. The prefill is a starting point, so change any of it.

## Schedule

The schedule dropdown lists the aliases in [cron schedules](schedules.md), such
as `@hourly` and `@daily`. To run on something the aliases don't cover, choose
**Custom** and type a five-field expression into the dialog. See
[custom cron expressions](custom-expressions.md) for the field order, the
operators, and the syntax that saves but never runs.

## Script

The script field is a bash editor. Type the script, or drag a `.sh` file onto
the editor to load its contents. Keep the `#!/bin/bash` line at the top: Amezmo
runs the script with `bash`, so the file mode doesn't matter, but the shebang
documents what the script expects.

Amezmo runs it as the `deployer` user from your
[current release](../deployments/directories.md) directory, with a small
environment:

`PATH`
: `/usr/local/bin:/bin:/usr/bin`. A binary outside those directories needs its
full path, or the run fails with `command not found`.

`APPLICATION_ROOT`
: The same release directory the script starts in, so you can reference it
without hard-coding a path that changes on every deployment.

`HOME`
: `/home/deployer`

`SHELL`
: `/bin/bash`.

`MAIL`
: Off. Cron sends nothing by email, and output goes to the entry's log instead.

Those are the variables the crontab sets, so don't count on your application's
[secrets](../secrets/index.md) being in the shell environment. Have the script
call into your application (`php artisan`, `drush`, a PHP script) and let the
application load its own configuration.

Keep the script itself thin. A cron entry that calls one command in your
repository means a change to the task ships with your next deployment instead of
an edit here.

## What happens when you save

The entry appears in the cron list right away, and Amezmo writes the script and
the crontab entry on your instance in the background. Saving does not run the
task once. The first run happens the next time the schedule matches, which for a
`@daily` entry created in the afternoon is the coming midnight.

> [!NOTE]
> To check that a new script works, save it with `@minutely`, watch the log on
> the entry page, then edit the entry and set the schedule you actually want.

## Creating over the API

[Create a cron entry](../api/cron/create-cron-entry.md) does the same thing over
the REST API. It takes the name, the script, and the schedule you would type into
the form, plus an explicit `environment`, and it returns the entry's ID and log
file path.
