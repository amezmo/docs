# Backup and Restore

Amezmo takes logical backups of your MySQL database, the kind you'd get from
``mysqldump``: a file of SQL statements you can restore anywhere. Use a backup
to copy production to your machine, to archive or to move data between
environments.

## On-Demand Backups

Create a backup any time from the Database tab. Amezmo produces a compressed
``.sql.gz`` file that you can download, or restore later from the dashboard.

## Automated Backups

On plans that include them, schedule automated backups from the Database tab
under automation settings. You choose:

- Which databases to back up. Backing up more than one needs a plan that
  supports multiple databases.
- The time of day the backup runs.
- How long to keep backups. Your plan sets the maximum retention, and the form
  tells you the limit.
- An optional encryption key, on plans that support
  [encrypted backups](encryption.md).

You can also get an email when a scheduled backup succeeds or fails.

> [!NOTE]
> If scheduled backups don't seem to run, check that your plan includes
> automated backups, that you selected at least one database, and that retention
> isn't set to zero.

## Restoring

Restore from a backup on the Database tab. You can:

- Upload a local ``.sql`` file, optionally compressed as ``.zip`` or
  ``.tar.gz``.
- Restore from a backup Amezmo already has.

When you restore, you can choose to overwrite the existing database or create a
new one.

## Cloning between Environments

To copy a database from one environment to another, such as production to
staging, see [environment cloning](../environments/cloning.md).
