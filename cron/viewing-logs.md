# Viewing cron logs

{.lead}
Everything a [cron entry](index.md) prints lands in a log file on your instance.
The entry page shows the end of that file, and you can download the whole thing
or export it to S3.

## Where the output goes

Each entry gets its own log file, named after the entry:

{title="Log file path"}
```bash
/home/deployer/cron/logs/cron.<entry-name>.log
```

Amezmo redirects both standard output and standard error into it and appends,
so every run adds to the end of the same file and the newest output is last. A
failing command shows up there too: `command not found`, a PHP fatal error, and
a non-zero exit's stderr all get written.

Nothing trims the file for you, so a chatty task on a frequent schedule writes a
large log over time. Print what you need to diagnose a run and no more.

## Reading the log in the dashboard

Open **Cron** and click the entry. The log sits below the script, under the
file's path.

The viewer shows the last 50 lines, read when the page loads. It does not update
on its own, so reload the page to see newer output. An entry that has not run
yet, or a script that prints nothing, shows `No Logs`.

Amezmo does not record a run history, a start time, or an exit status, so the
log is the record of what happened. Print your own markers if you want them:

{title="Timestamp each run"}
```bash
#!/bin/bash
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] starting"
php artisan schedule:run
status=$?
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] finished with status $status"
```

## Downloading and exporting

The menu on the log panel has two actions:

Download log file
: Amezmo prepares the full file and your browser saves it. Use this when the
last 50 lines aren't enough.

Export to S3
: Sends the file to your own bucket. It needs four secrets set first, see
[exporting logs](../logs/exporting.md).

Cron logs don't appear on the [Logs](../logs/index.md) tab, which lists your
application logs and your server logs. A cron log belongs to its entry and stays
on the entry's page.

You can also read the file directly over [SSH](../instances/ssh.md), which is the
one way to watch a run as it happens:

{title="Follow a cron log over SSH"}
```bash
$ tail -f /home/deployer/cron/logs/cron.Laravel-task-scheduler.log
```

## When the log is empty

An empty log means nothing has been written yet, which usually comes down to
one of these:

- The entry hasn't reached its first run. Check the schedule in
  [cron schedules](schedules.md), and remember the instance clock decides when
  the expression matches.
- The expression saved but never matches. See
  [custom cron expressions](custom-expressions.md) for the syntax that looks
  valid and never runs.
- The script succeeds and prints nothing. Add an `echo` to confirm it ran.
- You're looking at the wrong environment. An entry runs only in the environment
  it was [created in](creating-entries.md), so a production entry writes nothing
  in staging.

## Deleting takes the log with it

Deleting a cron entry removes its script, its crontab entry, and its log file
from the instance. Download the log first if you want to keep what it recorded.
That is also why an entry's name is fixed while it exists, see
[editing a cron entry](editing-entries.md).
