# Domain names

Amezmo automatically generates a SSL certiificate for each domain name you add. When creating an instance for the first
time, you are asked to provide a fully qualified domain name. You can provide any resolvable domain name, including subdomains.
Each application instance also gets an [Amezmo provided subdomain](/docs/domains/development-subdomain)

- [Development subdomain](/docs/domains/development-subdomain):
Use an Amezmo provided development domain instead of a custom domain
- [Wildcard SSL certificates](/docs/domains/wildcard-ssl-certificates)
- Websockets: Setup a worker process and point a domain name to it
- Fully automated: Amezmo generates and renews your certificate automatically
- Private certificates: Your certificates are not shared, or backed by a SAN certificate

## Validating your domain

After launching an instance, you can add your domain names. You will be required to point the DNS records to
Amezmo's server endpoint. The IP address will be provided for you on the Domains tab.

To validate a domain,
Amezmo will send a HTTP request to your domain name and inspect the response. Upon sending the HTTP request to your domain,
Amezmo will follow 301 or 302 redirects only 4 times. A domain name is successfully validated once
the system confirms that the DNS entry is pointed to the Amezmo server.

## Limits

- When validating your DNS A record for, Amezmo will follow only four 301 redirects