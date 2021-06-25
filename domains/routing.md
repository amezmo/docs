# Domain Routing

The first domain you add to Amezmo is automatically put into the validation queue. This first domain
name is assumed to be your primary application domain name.

The domain you provide when you launch an instance is routed to your Nginx server by default.
However, you can add and remove domain names
at anytime, before, or after they are validated.

## Routing Domains to Workers

You may also route a domain to one of your worker processes. Domain names cannot be used for more
than one worker process. Upon adding a domain name, ensure that the option "Route to Nginx" is left unchecked.

- Domains must be validated for Worker routing
- Domains can be attached to 1 worker process only