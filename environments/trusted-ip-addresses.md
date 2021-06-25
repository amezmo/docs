# Trusted IP Addresses

Trusted IP addresses are a set of known IP addresses. By default, your application is available to the entire Internet.
However, you may optionally limit which computers may access your application
by providing an IP safelist. Amezmo refers to these as Trusted IP Addresses.

Commonly, this feature is used to limit access to [staging environments](/docs/environments) Setting
a Trusted IP Address limits who can access your application from the Internet. When enabled and a request arrives
to your application from an untrusted IP address, your application will respond with 403 (Forbidden).

Trusted IP addresses apply to every domain in your environment. Per-path trusted IP addresses are not supported
at this time.

## Limits
- **IP address limit**: A maximum of 4 Trusted IP addresses may be provided.

    
