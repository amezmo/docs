# Trusted SSH IP Addresses

Setting Trusted IP addresses for SSH lets you control which computers can access your container.

These trusted IPs apply to SSH access only. To restrict who can reach your site over the web, see [Nginx trusted IP addresses](../environments/trusted-ip-addresses.md).

SSH is not fully enabled until you set at least one trusted IP address. By default, the trusted IP addresses
input will show you your IP address and give you the option of adding it to the list. 
When disabling SSH, all your trusted IP addresses will be deleted.

To set trusted IP addresses, navigate to Overview > SSH > Edit trusted IPs

![Edit trusted IP address](https://s3.us-east-2.amazonaws.com/static.amezmo.net/ssh-trusted-ips.png){.img-enlargable}


