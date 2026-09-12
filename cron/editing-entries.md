# Editing a cron entry

{.lead}
Change the script a [cron entry](index.md) runs, or how often it runs, without
recreating the entry.

## Editing from the dashboard

Open your instance, go to **Cron**, and open the entry you want to change. Click
**Edit** in the entry header, or pick **Edit** from the entry's menu in the cron
list.

The edit form is the same one you used to create the entry. Change the schedule,
the script, or both, then click **Save**.

## What you can change

Schedule
: Pick an alias such as `@hourly` from the dropdown, or choose **Custom** and
type an expression. See [custom cron expressions](custom-expressions.md) for the
syntax. An entry created with a custom expression comes back with that
expression already selected.

Script
: Edit the bash script in place, or drag a `.sh` file onto the editor to replace
it. Scripts still run from your
[current release](../deployments/directories.md) directory, so a script that
worked before an edit works after one.

## What you can't change

**The name is fixed.** Amezmo derives the entry's log file name from the name you
gave it, so a rename would leave the existing log stranded under the old name and
start a fresh, empty one. The name field is read-only on the edit form. If you
need a different name, delete the entry and create a new one, and keep in mind
that deleting removes the old log file with it.

**Editing doesn't move an entry between environments.** An entry belongs to the
environment it was created in. To run the same task in staging and production,
create an entry in each.

**An entry being deleted can't be edited.** Once you confirm a delete, the entry
is on its way out and the **Edit** action disappears from it.

## What happens when you save

Amezmo applies the change on your instance in the background: it rewrites your
script and the crontab entry in place. The entry keeps its ID and keeps writing
to the same log file, so the history you already have stays where it is.

The change is not instantaneous, and it is not transactional with a run in
flight. A run that has already started finishes under the old script. The next
run after the update lands uses the new one.

> [!NOTE]
> Editing the schedule doesn't run the task. If you want to confirm a new script
> works, give it a frequent schedule such as `@minutely`, watch the log on the
> entry page, then set the schedule you actually want.

## Editing over the API

[Update a cron entry](../api/cron/update-cron-entry.md) does the same thing over
the REST API, with the same limitations. It takes `command`, `expression`, or
both, and leaves out anything you omit.
