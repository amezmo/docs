# Domain Names

Amezmo generates and renews an SSL certificate for every domain you add. When
you launch an instance, you provide a fully qualified domain name, and you can
add more domains at any time. Each instance also gets an
[Amezmo development subdomain](development-subdomain.md).

- [Development subdomain](development-subdomain.md)
- [SSL certificates](ssl-certificates.md)
- [Wildcard SSL certificates](wildcard-ssl-certificates.md)
- [Domain routing](routing.md)
- [Redirects](redirects.md)
- [Rules](rules.md)

## Validating a Domain

After you add a domain, Amezmo checks that it points at your instance before it
issues a certificate. To validate, Amezmo sends an HTTP request to your domain
from a US IP address and confirms it reaches your instance. It follows up to
four 301 or 302 redirects. Amezmo retries validation on its own about every 30
minutes.

Point your domain at your instance with one of these records:

- An A record to your instance's public IP address.
- A CNAME record to your [development subdomain](development-subdomain.md).

The Domains tab shows the exact IP address and subdomain to use. A root domain
usually can't use a CNAME, so use the A record for the root and a CNAME for
subdomains.

## When Validation Fails

If validation keeps failing after you added the record, check these:

- Give DNS time to propagate. A new record isn't visible everywhere right away,
  and Amezmo keeps retrying, so you can wait.
- Confirm the record and value. The A record must be the exact IP shown on the
  Domains tab, and each instance has its own IP. The CNAME must be the exact
  development subdomain shown.
- Turn off proxying. If you run Cloudflare with the orange-cloud proxy on,
  public DNS resolves to Cloudflare instead of your instance, so Amezmo can't
  confirm the record. Set the record to DNS only (grey cloud).
- Allow the validation request. Amezmo's request comes from a US IP over HTTP
  and HTTPS. Disable any firewall rule that blocks standard web traffic during
  validation, then turn it back on afterward.
