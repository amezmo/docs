# Remote MySQL Access with SSH

If you launched an instance with MySQL support, the database is reachable from
that instance and from any instance shared with it. From the Amezmo dashboard
you can back up, restore and check its status.

First make sure [SSH is enabled](../instances/enable-or-disable-ssh.md) on your
instance, then go to Overview, then Server Details, then find your SSH port. An
example SSH command is below.

{title="SSH tunnel to MySQL"}
```bash
$ ssh -i <id_rsa> -p <your ssh port> \
    -L 127.0.0.1:3306:127.0.0.1:3306 \
    -N deployer@<internalDomain>lb2.amezmo.co
```

> [!IMPORTANT]
> When you connect with the SSH command, you reach your database over a secure
> SSH tunnel.

In this example the local IP address is ``127.0.0.1`` and the local port is
``3306``. If you already run a MySQL server on your local machine, change the
port in the command to something else, such as 3307.

## Requirements

Before you can reach your MySQL database over SSH, upload your public SSH key to
your instance. [Learn more](../instances/ssh.md) about accessing your instance's
resources through SSH.

## See Also

- [Remote database access](remote-access.md)
