# Enable or Disable SSH

From the Overview tab, you can enable or disable SSH access to your instance
with the green toggle. When SSH is off, your instance does not respond to SSH
requests.

Once SSH is on, see [connecting over SSH](ssh.md) for the login command and SFTP
details.

![Instance Overview tab showing the SSH access toggle and the list of added public keys.](https://s3.us-east-2.amazonaws.com/static.amezmo.net/SSHKeyList.png){.img-enlargable}

## SSH Port

Each instance gets a dedicated port for routing inbound requests into your
container. Containers are not exposed directly to the internet. Amezmo proxies
known requests into your container based on a set of trusted IP addresses. To
view your SSH port, go to Overview, then Server Details, then SSH Port.

## Public Keys

Add a public key from the Add public key button. In the modal, give your key a
name and paste the public key into the text area.

![Add public key modal with fields for a key name and the public key text.](https://s3.us-east-2.amazonaws.com/static.amezmo.net/SSHKeyForm.png){.img-enlargable}

## Limits

- 3 public keys per instance.
- Public-key authentication is the only allowed method.
- Root access is not available.

## See Also

- [Remote MySQL access with SSH](../databases/ssh.md)
