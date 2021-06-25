# Sharing MySQL with other instances

Your MySQL server, as well as other services, can be accessed from another instance attached to your private network. On Amezmo,
this is called "instance sharing". It joins one instance with one or more instances into the same private network.

When you first launch an instance,
you have the option to "share" the instance with another instance you own. The effect of this is
the newly created instance is attached to the network of the instance you choose to share with.

## Notes about MySQL

- **Usernames**: 
The user `az_user` is created at instance creation time. The MySQL server will accept **non-ssl** connections **only** from connection requests within your private subnet.

- **Remote connections**: 
Internet-based connections to your MySQL server require X509 authenticaiton as well as a white-listed IP address.
