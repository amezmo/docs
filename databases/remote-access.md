# Remote Database Access

Your MySQL server isn't reachable from the public internet by default. You can
still connect a local MySQL client in one of two ways.

## SSH Tunnel

Any plan with SSH can reach MySQL through an SSH tunnel. You open a tunnel to
your instance, then point your MySQL client at ``127.0.0.1``. This is the
simplest way to pull your production data to your machine. See
[Remote MySQL access with SSH](ssh.md) for the steps.

## Remote MySQL

Remote MySQL opens a database port to a list of trusted IP addresses, so you can
connect a client directly without a tunnel. It's a paid feature. Turn it on from
the Database tab under Remote access, add the IP addresses allowed to connect,
and download the SSL certificate files for a secure connection.

## Connecting

Use the Internal host shown on the Database tab, not an IP address, because the
IP can change. To reset your database password, open the Database tab, then
Database configuration, then Change. A password change applies to every
environment on the instance.
