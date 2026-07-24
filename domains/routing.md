# Domain Routing

The first domain you add to Amezmo goes into the validation queue automatically,
and Amezmo treats it as your primary application domain.

The domain you provide when you launch an instance routes to your Nginx server
by default. You can add and remove domains at any time, before or after they are
validated.

## Routing Domains to Workers

You can also route a domain to one of your worker processes. When you add the
domain, leave the "Route to Nginx" option unchecked.

- Domains must be validated for worker routing.
- A domain can be attached to one worker process only.

To mark a path for WebSocket connections, add a [domain rule](rules.md).
