# Databases

Amezmo runs a dedicated MySQL server (5.7 or 8.0) for instances launched with
database support. From the dashboard you can back up, restore and check the
status of your database, and any instance shared with the database instance can
reach it. Your MySQL server is never reachable from the public internet.

- [MySQL](mysql.md)
- [Redis](redis.md)
- [Remote access](remote-access.md)
- [Remote MySQL access with SSH](ssh.md)
- [SSL connections](ssl-connections.md)
- [Passwords](passwords.md)
- [Backup and restore](backup-restore.md)
- [Instance sharing](instance-sharing.md)
- [Encryption](encryption.md)

## Connecting

Connect from your app using the Internal host shown on the Database tab, not an
IP address. The internal hostname is stable, while the database host's IP can
change.
