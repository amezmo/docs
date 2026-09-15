# Custom cron expressions

{.lead}
When none of the [schedule aliases](schedules.md) fits, write a five-field
cron expression instead. This page covers the syntax Amezmo accepts, the parts
of it that look valid but never run, and a set of expressions you can copy.

In the dashboard, open a cron entry's schedule dropdown, choose **Custom**, and
type the expression into the dialog. Over the API, send the same string as the
`expression` field of
[Create a cron entry](../api/cron/create-cron-entry.md) or
[Update a cron entry](../api/cron/update-cron-entry.md).

## The five fields

An expression is five fields separated by spaces. Each field says which values of
that unit the entry runs on, and the entry runs when every field matches.

{title="Field order"}
```bash
# minute  hour  day-of-month  month  day-of-week
    30     2         *          *         *
```

Field        | Range   | Notes
------------ | ------- | -----------------------------------------------
minute       | `0-59`  |
hour         | `0-23`  | Midnight is `0`, not `24`
day of month | `1-31`  |
month        | `1-12`  | Or `JAN` through `DEC`
day of week  | `0-7`   | `0` and `7` are both Sunday. Or `SUN` through `SAT`

Names are not case sensitive, so `mon` and `MON` both work. You can't use a name
in a step, so write `1-5` rather than `MON-FRI/1`.

## Operators

`*`
: Every value of the field. `* * * * *` is every minute of every day.

`,`
: A list. `0 8,12,18 * * *` runs at 08:00, 12:00, and 18:00.

`-`
: A range. `0 9-17 * * *` runs hourly from 09:00 through 17:00, inclusive.

`/`
: A step through a range. `*/15 * * * *` runs at minutes 0, 15, 30, and 45.
`0 9-17/2 * * *` runs at 09:00, 11:00, 13:00, 15:00, and 17:00.

A step counts from the start of its range, not from the current time. `*/40` in
the minute field fires at minute 0 and minute 40, then waits 20 minutes, because
the range restarts every hour. Steps that don't divide evenly into their range
are uneven like this, which is why `*/15` is a safer habit than `*/40`.

## Examples

Expression      | Runs
--------------- | ------------------------------------------------
`*/10 * * * *`  | Every ten minutes
`0 * * * *`     | At the top of every hour
`30 2 * * *`    | Every day at 02:30
`0 9-17 * * 1-5`| Hourly from 09:00 to 17:00, Monday through Friday
`0 3 * * 0`     | Sundays at 03:00
`0 0 1 * *`     | Midnight on the first of the month
`0 0 1 1 *`     | Midnight on January 1
`15 4 1,15 * *` | 04:15 on the 1st and the 15th

## Limitations

### Amezmo accepts syntax your instance won't run

The dashboard validates your expression with a PHP parser that understands
Quartz-style extensions. Standard Linux cron, which is what actually runs the
entry on your instance, does not. So these save without complaint and then never
fire:

Not supported | What it means elsewhere
------------- | -------------------------------------
`L`           | Last day of the month or the week
`W`           | Nearest weekday to a date, as in `15W`
`#`           | Nth weekday of the month, as in `5#3`
`?`           | No specific value

Stick to `*`, `,`, `-`, `/`, numbers, and month or weekday names. If you need
"last day of the month", schedule the entry daily and exit early from your
script instead:

{title="Run only on the last day of the month"}
```bash
#!/bin/bash
# Tomorrow is the 1st, so today is the last day of this month.
if [ "$(date -d tomorrow +%d)" != "01" ]; then
    exit 0
fi

php artisan billing:close-month
```

### Day of month and day of week are an OR, not an AND

When both the day-of-month and the day-of-week fields are restricted, cron runs
the entry when **either** matches, not when both do. `0 0 13 * 5` runs on the
13th of every month *and* on every Friday, not only on Friday the 13th. Leave one
of the two as `*` unless you want that behavior.

### `@reboot` and seconds are not supported

Amezmo rejects `@reboot`: a cron entry is a schedule, not a startup hook. Use a
[worker](../workers/index.md) for a process that should run continuously and come
back after a restart.

There is no seconds field. One minute is the shortest interval an expression can
express. If you need to act more often than that, loop inside your script or run
a worker.

### Schedules follow the instance clock

Cron matches your expression against your instance's system clock, and you can't
set a timezone per entry. Check what your instance thinks the time is over
[SSH](../instances/ssh.md):

{title="Check the instance clock"}
```bash
$ date
```

If your task's timing has to follow a specific timezone, set `TZ` inside the
script for the commands it runs, and pick the expression to match the instance
clock.

### Editing the schedule doesn't reschedule a running task

Saving a new expression rewrites the entry on your instance in the background. A
run already underway finishes on the old schedule's terms. See
[Editing a cron entry](editing-entries.md).

## Checking your work

The entry page streams the task's log, so the fastest way to confirm an
expression is to save it, wait for the first window, and watch the log. Give a
new script a frequent schedule such as `@minutely` while you're testing it, then
switch to the real one.
