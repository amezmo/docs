# Enable/Disable SSH

From the Overview tab, you can enable or disable SSH access to your instance by switching the green knob. When SSH
is turned off, your instance will not respond to SSH requests.

Once SSH is enabled, see [connecting over SSH](ssh.md) for the login command and SFTP details.

![Instance Overview tab showing the SSH access toggle and the list of added public keys](https://s3.us-east-2.amazonaws.com/static.amezmo.net/SSHKeyList.png){.img-enlargable}

## SSH port

Each instance on Amezmo is allocated a dedicated port that's used for routing inbound requests into your container.
Containers aren't exposed directly to the Internet. Amezmo proxies known requests into your container securely based on a set of trusted IP addresses. To view your SSH port,
go to Overview > Server Details > SSH Port.

## Public keys

Add a public key to your server by clicking the Add public key button. After being presented with the modal,
give your key a name and paste your public key into the text area.

![Add public key modal with fields for a key name and the public key text](https://s3.us-east-2.amazonaws.com/static.amezmo.net/SSHKeyForm.png){.img-enlargable}

## Limits
- 3 public keys per instance
- Public/Private Key authentication is the only allowed authorization method
- Root access is not implemented

## See also

- [Remote MySQL access with SSH](../databases/ssh.md)
