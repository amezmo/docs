# Payment Methods

Manage the cards on your account from Billing > Payment methods. You can add a
card, choose your default and remove cards you no longer use.

## Adding a Card

Open Billing > Payment methods, enter your card details and save. Your first
card becomes your default automatically. Amezmo charges the default card for
your monthly [hourly usage](hourly.md).

## Changing the Default Card

Add the new card if you haven't already, then set it as the default from
Billing > Payment methods. Amezmo charges the default card for your usage.

## Removing a Card

You can remove any card except your current default. To replace the default,
add the new card and set it as the default first, then remove the old one.

## Fixing a Past-Due or Failed Payment

A charge can fail for a few reasons, like an expired card, insufficient funds
or a charge your bank blocked. When that happens, your account becomes past
due and the dashboard shows a banner asking you to update your billing
details.

To fix it, go to Billing > Payment methods and add a working card or update
your existing one, then make sure it's the default. Adding a card or changing
your default tells Amezmo to retry your outstanding invoices right away, so
there's no separate pay button. Once a retry succeeds, the past-due state
clears on its own. If the same card keeps failing, add a different card
instead of retrying it.

While your account is past due you can't launch, start or resize
[instances](../instances/index.md), and Amezmo blocks API access.

> [!WARNING]
> If the balance stays unpaid, Amezmo might pause your running instances and
> then terminate them after 14 days.

## Adding Funds in Advance

To keep a positive balance instead of paying at the end of the month, add
funds ahead of time with [Advanced Pay](advanced-pay.md).
