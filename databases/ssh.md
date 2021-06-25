# Remote MySQL access with SSH

If you've chosen to launch an instance with MySQL support,
then MySQL will available directly, and with any instance on the shared network. From the
Amezmo dashboard, you can backup, restore, and check the status of your database.

After ensuring that
[SSH is enabled](/docs/instances/ssh#enable-ssh) on your instance,
then go to Overview > Server Details and find your **SSH port**. An example SSH command is provided for you below:


```bash
ssh -i <id_rsa> -p <your ssh port>  \
    -L 3306:127.0.0.1:3306 \
    -N deployer@<internalDomain>lb2.amezmo.co
```

**Important**: When you connect to your instance with the SSH command, you'll be able to access
your database over a secure SSH tunnel.


In this example command, the local IP address is `127.0.0.1`, and the local port
is `3306`.
If you're already running a MySQL server on your local machine, be sure to change the port in the command to something else, such as 3307.

## Requirements

Before you can access your MySQL database via SSH, you must upload your public SSH key to your instance.
[Learn more](/docs/instances/ssh) about accessing your instances resources through SSH.


