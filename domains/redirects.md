# Domain Redirects

A redirect sends visitors from one domain to another. On Amezmo a redirect works
between two domains on the same instance, and it redirects the whole host rather
than a single path.

## Requirements

Both domains must be added to the instance and fully validated, which means each
one has its SSL certificate. See [SSL certificates](ssl-certificates.md) for how
validation works.

## Creating a Redirect

1. Open the Domains tab and click the domain you want to redirect from.
2. In the domain menu, choose Redirect this domain.
3. Pick the destination from your instance's other domains.
4. Choose the status code: 301 for a permanent redirect, or 302 for a temporary
   one.

Amezmo applies the redirect a moment later. To undo it, choose Remove redirect
from the same menu.

## Rules to Know

- You can't redirect to a wildcard domain. Use a specific domain instead.
- The source and destination can't be the same domain.
- You can't create a loop. If example.com redirects to example.net, then
  example.net can't redirect back to example.com.
- A domain that is a redirect target can't be deleted while the redirect exists.
  Remove the redirect first.
