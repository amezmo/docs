# Domain Rules

A domain rule attaches an action to a path on a validated domain. Today the
available action is Websocket, which marks a path so the server handles
WebSocket connections there. It pairs with pointing a domain at a worker
process. See
[Domain routing](routing.md).

## Creating a Rule

1. Open the Domains tab and click the domain.
2. Open the create-rule form and enter the path.
3. Choose the Websocket action.

The path accepts letters, digits, ``_``, ``-`` and ``*``, with no slashes.
Amezmo adds the leading slash for you.

To remove a rule, delete it from the domain's rules table.
