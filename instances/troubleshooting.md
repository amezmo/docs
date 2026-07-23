# Instance Troubleshooting

This page covers what to do when an instance won't launch or the launch seems to
stall.

## A Launch is Refused

Amezmo checks a few things before it builds an instance. If one fails, the
launch stops with a message that tells you what to fix:

- "Please add a payment method first." Add a card under Billing, then try again.
  See [Payment methods](../billing/payment-methods.md).
- "Your payment method could not be verified." Your card was declined or
  flagged. Add a working card. See [Payment methods](../billing/payment-methods.md).
- "Amezmo is unable to complete this request because your account is past due."
  Pay the outstanding balance, then launch. See
  [Payment methods](../billing/payment-methods.md).
- "Please contact support to get your account limit increased." You reached the
  number of apps your account can run. See [Instance limits](limits.md).
- "This region is at capacity. Please contact support." Pick another region, or
  contact support to launch in that one. See [Regions](regions.md).
- "You cannot share with this instance because your new instance will be
  launched into a different data center." A shared instance must be in the same
  region. See [Sharing](sharing.md).

## A Launch Seems to Hang

When you launch an instance, Amezmo queues the real work (building the
container, setting up the database and SSL) on the region's hardware. The
progress bar tracks that background job, not your browser, so expect it to sit
for a bit.

If it stays stuck well past that, contact support with your instance name. There
is no separate retry to run yourself, so support is the fastest path.
