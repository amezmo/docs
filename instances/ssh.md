# SSH Access

Amezmo runs SSH through a secure entry-point host. It routes your connection
from the load balancer straight to your instance on a pre-allocated port. See
[enabling SSH](enable-or-disable-ssh.md) to turn it on and find your port.

## SSH Command

{title="SSH command"}
```bash
$ ssh -i <path to your private key> -p $PORT deployer@$DOMAIN.lb2.amezmo.co
```

- ``-i`` is the path to your private key file. When you
  [enable SSH](enable-or-disable-ssh.md) you add a public key, and every public
  key has a matching private key. Together they are a public and private key
  pair.
- ``-p`` is your SSH server's port. Amezmo allocates a unique port for your
  inbound SSH sessions, shown on your instance's Overview page.

## SFTP Command

{title="SFTP command"}
```bash
$ sftp -i <path to your private key> -P $PORT deployer@$DOMAIN.lb3.amezmo.co
```

Your dashboard shows the ``$DOMAIN`` variable. It is the part before your
[internal domain](../domains/development-subdomain.md). To find your SSH port,
see the [SSH port](enable-or-disable-ssh.md#ssh-port) page.

## Windows PuTTY Application

### Session

Hostname: ``$DOMAIN``.lb3.amezmo.co

Port: ``$PORT``

Connection type: ssh

### Authentication

In Connection, then SSH, then Auth, browse to the local file with your private
key.

## Limits

- Root access is not available.
- Public-key authentication is the only supported method.

## See Also

- [SSH troubleshooting](ssh-troubleshooting.md)
- [Remote MySQL access with SSH](../databases/ssh.md)
