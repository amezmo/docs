# Encrypted environment variables (Secrets)

Secrets, or encrypted environment variables, let you store sensitive information such as API keys, license keys, and other strings that should not be stored in plain-text. 

Secrets are encrypted on the client-side before sending them to Amezmo, and are decrypted in-memory using a private key. Secrets are automatically
injected into [deployment hooks](/docs/deployments/hooks)
Secrets are defined in the Configuration section
within your Amezmo dashboard.


- [How secrets work](/docs/secrets/how-secrets-work)
