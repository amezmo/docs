# Nginx Trusted IP Addresses

Trusted IP addresses are an optional security feature you can turn on or off at
any time. By default, your web server is available to everyone.

> [!NOTE]
> To keep your SSH access working, see
> [SSH trusted IP addresses](../instances/trusted-ip-addresses.md).

## How Trusted IP Addresses Work

Trusted IP addresses are a set of known IP addresses you provide. By default,
your application is open to the entire internet. When you set a safelist, Amezmo
blocks any request whose IP address is not on it.

## Site Behavior When Trusted IP Addresses Are Set

This feature is often used to lock down [staging environments](index.md). When a
request arrives from an untrusted IP address, your application responds with a
403 Forbidden.

Trusted IP addresses apply to every domain in your environment. Per-path trusted
IP addresses are not supported.

## Limits

IP address limit
: You can provide a maximum of 4 trusted IP addresses.
