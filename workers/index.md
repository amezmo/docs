# Workers
Workers are long running proccesses that are intended to always be running. Amezmo manages the logging,
stopping, restarting, and monitoring of your workers. 

Common use cases for workers are background processing queues, email queues, and othe asynchronous processing activities.

For PHP applications, Amezmo can automatically create the queue command for
[Laravel queues](https://laravel.com/docs/queues)

## Managing workers
Amezmo logs worker output to a standard location in your container. This is located in `/backups/logs`.
Of course, the exact log path will be different for each of your workers, but you can always view the exact path
on each Worker summary page in the dashboard.

Worker log files are capped at 2MB and are automatically rotated upon reaching this limit. Amezmo keeps a maximum
of 2 log file backups. `stdout` and `stderr` are logged to the same file. Amezmo redirects
`stderr` to `stdout` automatically. Therefore, there will only be 1 log file that represents
both output streams.

## Routing inbound HTTP requests to Workers
Workers can be categorized into 2 groups. The first group, is an *isolated worker*, which does not 
accept inbound HTTP traffic. For example, a worker that processes async email sending jobs would not need to accept inbound HTTP requests.

The second type,
is a *routable worker*, which means HTTP requests are forwared into the worker process. The most common example of this would be a
Node.js process that runs a Websocket server. Inbound HTTP requests on your domain would be routed into the worker.

## Supported Runtimes

Workers can be any process. The command that you provide when
creating a worker can be a path to a PHP script, a CLI command, or any other
path to a script from a supported runtime. The following runtimes are officially supported on Amezmo.

- Node.js and NPM
- PHP