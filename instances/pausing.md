# Pausing

Pausing an instance takes it offline, but doesn't [terminate](/docs/instances/terminating) it.
The instance is shutdown and inbound requests
to the instance will not be possible. Pausing is similar to shutting down your own computer.

Of course, upon pausing
your instance on Amezmo, your data will be persisted. Then, when you start your instance, your data will be in the
same state as it was when you paused it.

When an instance enters the paused state, database backups will not be attempted, 
and no automated database backup record will be created during the time that the instance is paused.

To bring your instance back up, press the Start button on the instance Overview page.

<p class="alert alert-info">
   <b>Note</b>: Instances in a Paused state will still incur the hourly charge.
</p>
