# Instance Sharing

You can share an application with other [instances](index.md) on Amezmo, which
joins your instance to another instance's private network.

When you share, the instance you configure gets a new IP address inside the peer
instance's network range. The two instances then become peers on one network.
The requester, the instance you configure sharing on, is the one whose IP
changes, not the receiver.

A shared instance must run in the same [region](regions.md) as its peer.
