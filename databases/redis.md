# Redis

If you've chosen Redis at instance creation time, then you'll have a Redis server available. This instance of
Redis can be access from any of your shared instances. Redis is not exposed to the Internet.

Redis data is not persisted. Redis on Amezmo is designed to be used for in-memory caching only, and long-term data
should not be stored in Redis, as it will be lost upon restarting your instance. You must use a database
for persistent storage.


<div class="alert alert-info">
    <b>Note</b>: If you chose Redis in the application creation wizard, then Redis is installed
    and listening on the default port. See
    <a href="/docs/instances/ports-and-ip-addresses">ports and IP addresses</a> for more information.
</div>