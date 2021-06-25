# Environment directory

Environments are logically separated applications within one instance. To maintain this isolation,
various directories are separated.
Among others, the [release, storage, node_modules, and vendor directories](/docs/deployments/directories) are located within an environment root directory.
The default environment, Production, is always located under 
`/webroot`, but Staging is located in a separate directory
under webroot.

