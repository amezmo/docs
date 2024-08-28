#  Nginx Trusted IP Addresses

Trusted IP addresses for Nginx is an optional security feature on Amezmo that you can enable or disable at anytime. 
By default, your web server is available to everyone.

<div class="alert alert-info">
    <b>Note</b>: To ensure you can access SSH, see <a href="/docs/instances/trusted-ip-addresses">SSH Trused IP Addresses</a>
</div>


## How Trusted IP Addresses Work

To lock down your site, Amezmo lets you block all access to Nginx by default 
if the incoming ip address does not match a trusted ip. 
Trusted IP addresses. are a set of known IP addresses which you provide. 
By default, your application is available to the entire Internet.
However, you may optionally limit which computers may access your application
by providing an IP safelist. Amezmo refers to these as Trusted IP Addresses. 

## Site Behavior When Trusted IP Addresses are Set

Commonly, this feature is used to limit access to [staging environments](/docs/environments) Setting
a Trusted IP Address limits who can access your application from the Internet. When enabled and a request arrives
to your application from an untrusted IP address, your application will respond with 403 (Forbidden).

Trusted IP addresses apply to every domain in your environment. Per-path trusted IP addresses are not supported
at this time.

## Limits

<dl>
    <dt>IP address limit</dt>
    <dd>Maximum of 4 Trusted IP addresses may be provided.</dd>
</dl>
