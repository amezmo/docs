# Backup and Restore

By default, Amezmo installs MySQL 5.7 on your instance. This installation is optimized for security and performance. Backups are user-initiated.

Amezmo offers logical backups to be taken from user-initiated process.
This type of backup is commonly known as a "Database dump" which is a file consisting of
SQL statements such as `CREATE TABLE`, `INSERT` and `CREATE DATABASE`.
This backup can be used to replicate your production environment on your local machine and for archiving purposes.


## Restoring from a local backup

You may restore a database from a local backup file into your Amezmo instance by providing a backup file.
The file should be the same type of file you would use to restore the database on your local machine. 

Amezmo supports
`.sql` files that you'd produce with a command line utility such as [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html). This .sql file may optionally be compressed into a .zip or .tar.gz archive.
From the Amezmo dashboard you may provide a `.zip`, `tar.gz`, or a `.sql` file.


## Encrypted backups

You may optionally have your backups encrypted with an encryption key of your choice.
[Learn more](/docs/databases/encryption).
