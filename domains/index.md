# Domain Names

Amezmo generates and renews an SSL certificate for every domain you add. When
you launch an instance, you provide a fully qualified domain name, and you can
add more domains at any time. Each instance also gets an
[Amezmo development subdomain](development-subdomain.md).

## In This Section

### Development Subdomains

Every instance gets its own [development subdomain](development-subdomain.md)
on `amezmo.co`, served over HTTPS with a free
[SSL certificate](ssl-certificates.md) like any custom domain. Use it for
testing, or as your application's primary domain.

### SSL Certificates

Amezmo issues a [free Let's Encrypt certificate](ssl-certificates.md) for every
domain once it validates, and renews it for as long as the domain stays on the
instance.

### Wildcard SSL Certificates

A [wildcard certificate](wildcard-ssl-certificates.md) covers a domain and all
of its direct subdomains at once, so `*.example.com` secures `app.example.com`
and `api.example.com` together.

### Domain Routing

Domains reach your Nginx server by default.
[Domain routing](routing.md) covers pointing one at a worker process instead.

### Domain Redirects

A [redirect](redirects.md) sends visitors from one domain to another on the same
instance. Both domains have to be added and validated first.

### Domain Rules

A [domain rule](rules.md) attaches an action to a path on a validated domain,
such as marking a path for WebSocket connections.

## Validating a Domain

After you add a domain, Amezmo checks that it points at your instance before it
issues a certificate. To validate, Amezmo sends an HTTP request to your domain
from a US IP address and confirms it reaches your instance. It follows up to
four 301 or 302 redirects. Amezmo retries validation on its own about every 30
minutes.

Point your domain at your instance with one of these records:

- An A record to your instance's public IP address.
- A Canonical Name (<abbr title="Canonical Name">CNAME</abbr>) record to your [development subdomain](development-subdomain.md).

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
