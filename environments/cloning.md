# Cloning Environments

Amezmo can copy an environment, or just its database, so you can spin up a new
environment from an existing one or refresh staging with production data.

## Cloning a Whole Environment

On Advanced instances you can clone a full environment from the instance Actions
menu. Pick the environment to copy from, give the new environment a unique name,
and choose its branch. Amezmo copies:

- The Git connection, deploy key and chosen branch.
- The environment variables.
- The database, including schema and data.
- Deployment settings, health checks, alerts and trusted IP addresses.

The new environment then runs a deployment. Cloning a full environment is only
available on Advanced instances.

## Cloning a Database between Environments

To copy just the database from one environment into another, such as production
into staging, use Clone database on the
[Backup and restore](../databases/backup-restore.md) screen. Pick the source
environment and database, and Amezmo copies that database into the environment
you're viewing. The source and target can't be the same environment.

This copies the database only, not your code or environment variables.
