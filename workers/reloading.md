# Reloading Workers

After each successful deployment, your workers will be reloaded. Workers are always run from your [/webroot/current](/docs/deployments/directories) directory effectively always running the latest release of your code. Reloading is required because Amezmo has no way to determine if your worker code has changed or not.

## Configuration

Upon [changing your DotEnv configuration](/docs/configuration),
your workers will also be reloaded.

## Signals

Amezmo will send the `SIGINT` signal to your worker process upon reloading. We recommend
writing code to listen for this signal and gracefully
re-execute the process yourself. By handling the `SIGINT` signal,
you can be sure that the worker process does not exit in the middle of a critical section. By default,
Amezmo will wait 10 seconds for your worker process to shutdown before sending a final `SIGKILL` signal.
You may configure optionally configure this value to something higher, or lower.
