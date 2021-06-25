# How secrets work

Secrets are client-side encrypted variables that are automatically injected into deployments hooks. Commonly used to
store access keys and other sensitive strings such as API keys, and license keys that are not checked into source code.
The primary use case for secrets is for accessing a sensitive values during the deployment process.

Secrets are encrypted within the Amezmo dashboard on the client-side. Upon saving a secret, the encrypted value is sent
to Amezmo. Amezmo never stores the unencrypted value. Secrets are decrypted in-memory using the private key that
exists in your instance in your home directory. Amezmo doesn’t have access to the private key directly.
Upon terminating an instance, the private key is destroyed and it is never recycled.
