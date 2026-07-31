# Wildcard SSL Certificates

{.lead}
A **wildcard SSL certificate** secures a domain and all of its direct
subdomains with one certificate, so `*.example.com` covers `app.example.com`,
`api.example.com` and every other subdomain at that level. Amezmo issues
wildcard certificates from Let's Encrypt, the same authority it uses for
[standard certificates](ssl-certificates.md).

## When to Use One

A standard certificate covers a single domain name. A wildcard certificate fits
an application that serves many subdomains from one instance, such as a
multi-tenant app that gives each customer its own subdomain. One wildcard
certificate replaces a separate certificate for each subdomain.

## DNS Validation and API Credentials

A wildcard certificate validates over DNS instead of the HTTP challenge a
standard certificate uses. Let's Encrypt confirms you control the domain by
reading a DNS record, so Amezmo needs API access to your DNS provider to create
that record. You supply an API credential from a supported provider, and Amezmo
handles the record and the certificate request.

## Supported DNS Providers

Amezmo issues wildcard certificates through these providers. The links open each
provider's instructions for creating an API credential:

- [Cloudflare](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)
- [DigitalOcean](https://docs.digitalocean.com/reference/api/create-personal-access-token/)
