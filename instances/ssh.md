# SSH access

SSH is implemented through Amezmo's secure
entry point host. We securely route your connection from our load balancer directly to your instance using a
pre-allocated port. Learn more about [enabling ssh](/docs/instances/enable-or-disable-ssh) access and finding your port.


```bash
ssh -i <path to your private key> -p <your port> deployer@lb2.amezmo.co
```

## SSH command line arguments
- `-i` This argument contains the path to your private key file. When
        you [enable SSH](/docs/instances/enable-or-disable-ssh), you must add a public key. Every public key has a private key as well. These are referred to as a public/private key pair.
- `-p` This is the port of your SSH server. Amezmo allocates a unique port for your inbound SSH sessions.
        This can be found on your instance's Overview page.

## Limits
- Root access is not implemented
- Public Key authentication is the only supported method of authentication

