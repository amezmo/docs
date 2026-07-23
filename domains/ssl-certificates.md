# SSL Certificates

Amezmo issues a free SSL certificate for each domain after it validates. See
[Domain names](index.md) for how validation works. Once your domain validates,
Amezmo requests a certificate from Let's Encrypt and renews it automatically for
as long as the domain stays on your instance. If you delete the domain, the
certificate stops renewing.

## When a Certificate Won't Issue

A standard certificate uses an HTTP challenge, so your domain has to resolve
straight to your instance while the certificate is issued:

- Turn off any proxy. With Cloudflare's orange-cloud proxy on, the challenge
  can't reach your instance and the certificate fails. Set the record to DNS
  only until the certificate issues.
- Read the certificate output. When an attempt fails, the domain page shows an
  SSL certificate output block with the exact Let's Encrypt error. Start there.

If you already have a certificate and want a fresh one, remove and re-add the
domain, because Amezmo won't request a second certificate for a domain that
already has one.

## HTTPS and Redirects

Two separate switches control HTTPS on a domain, and both need a certificate
first:

- SSL serves your domain over HTTPS. You can turn it on only after the
  certificate is acquired. With SSL off, HTTPS requests to the domain don't
  work.
- Always use HTTPS redirects every HTTP request to HTTPS for the whole domain.

The order matters. The redirect control appears only while SSL is on. If your
HTTP traffic isn't redirecting even though you set it before, turn SSL on, make
sure the certificate is acquired, then turn Always use HTTPS on again.

## Cloudflare Free Tier

> [!WARNING]
> On the Cloudflare free tier, sub-subdomains aren't covered by their
> certificate. Buy a dedicated certificate from Cloudflare, or turn off
> proxying.

For a certificate that covers every subdomain, see
[wildcard SSL certificates](wildcard-ssl-certificates.md).
