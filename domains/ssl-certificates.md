# SSL Certificates

The Amezmo domain name system supports adding and removing domain names to your instances in real time. When you
add a domain name to your instance, it is immediately queued for validation.
Validating domain names on Amezmo has one requirement. One of the following requirements must be met.


- DNS A record for your domain must point to Amezmo
- CNAME record to your [development subdomain](/docs/domains/development-subdomain)

<div class="alert alert-info">
    **Note**: To find the public IP address that you'll need for your DNS A records, go to the Domains, then click on your domain the domain name table.
</div>

After validation succeeds, a new SSL certificate is requested from LetsEncrypt. This certificate
is renewed automatically, as long as your domain remains in the Amezmo system. If you delete your
domain, then the certificate will not renew after its expiration date


<p class="alert alert-warning">
    If you're using Cloudflare, know that sub-subdomains are not supported by the CloudFlare free tier. You must either buy a dedicated certificate from them, or turn off proxying.
</p>

## Resources
[CloudFlare SSL not working on sub-subdomains](https://community.cloudflare.com/t/ssl-certificate-not-working-on-second-subdomain/101819)