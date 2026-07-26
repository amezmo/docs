# SSH Troubleshooting

This page covers connection failures when you SSH into your instance, especially
"Permission denied (publickey)".

## Before Connecting

Check these first:

- SSH is on. Turn it on from the Overview tab and give it a moment, because
  enabling runs in the background.
- Your public key is added. Add it from the SSH panel on Overview, and connect
  with the matching private key. You can have up to three keys.
- Your IP is allowed. If you set SSH trusted IP addresses, only those addresses
  can connect, so add your current IP. The panel pre-fills it for you.
- You're using the right target. Connect as ``deployer`` on the port Amezmo
  shows, not as ``root`` and not on port 22.

## Permission Denied (publickey)

This means the server rejected your key. Work through the checklist above:

- If you just turned SSH on, wait a moment and retry.
- Make sure the public key on Amezmo matches the private key you connect with,
  and that the key shows in the list.
- Confirm you're connecting as ``deployer`` on the port shown on Overview.

## Connection Timed Out or Refused

The connection is blocked before it reaches your key, usually by the trusted IP
list. Add your current public IP under the SSH trusted addresses.

## Where to Find the Command

The SSH panel on the Overview tab shows the exact command to run, including your
port and host, and the Server details section shows the SSH port. See
[SSH access](ssh.md) for the command format, or
[Remote MySQL access with SSH](../databases/ssh.md) to connect a database client
through the same tunnel.
