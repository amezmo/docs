# Resource policy

Containers are allocated a memory reservation and a swap allocation. If the total memory is exceeded, the container will be killed.
Container restarts do not happen automatically. Excessive Out of Memory (<abbr title="Out of Memory">OOM</abbr>) events will result in the container being shut down.

## Out of Memory Policy
Amezmo may take the following actions when an OOM event happens.

- Increase the memory of your instance automatically
- Shutdown the instance to prevent excessive OOM events
