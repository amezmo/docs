# SSH access

SSH is implemented through the Amezmo secure
entry point host. Amezmo securely route your connection from our load balancer directly to your instance using a
pre-allocated port. Learn more about [enabling ssh](/docs/instances/enable-or-disable-ssh) access and finding your port.


## SSH command
```bash
ssh -i <path to your private key> -p $PORT deployer@$DOMAIN.lb2.amezmo.co
```

- `-i` This argument contains the path to your private key file. When
        you [enable SSH](/docs/instances/enable-or-disable-ssh), you must add a public key. Every public key has a private key as well. These are referred to as a public/private key pair.
- `-p` This is the port of your SSH server. Amezmo allocates a unique port for your inbound SSH sessions.
        This can be found on your instance's Overview page.

## SFTP command
```bash
sftp -i <path to your private key> -P $PORT deployer@$DOMAIN.lb3.amezmo.co
```

The `$DOMAIN` variable above can be found from your dashboard. It is the part before your [internal domain](/docs/domains/development-subdomain). To find your SSH port, please see the [SSH port](/docs/instances/enable-or-disable-ssh#ssh-port) page

## Windows Putty application

#Session
**Hostname**: $DOMAIN.lb3.amezmo.co
**Port**: $PORT
**Connection type**: ssh

## Connection -> SSH -> Auth
**Private key for authentication**: Browse to local file with private key

## Limits
- Root access is not implemented
- Public Key authentication is the only supported method of authentication
