# Encrypted Environment Variables (Secrets)

Secrets are encrypted environment variables for sensitive strings like API keys
and license keys that shouldn't be stored in plain text. Your browser encrypts a
secret before it reaches Amezmo, and your instance decrypts it in memory with a
private key that Amezmo can't read.

Amezmo injects secrets into your
[deployment hooks](../deployments/hooks/index.md), and they take effect on your
next deployment, not while your app is running. You manage them from the
Configuration section of your dashboard.

- [How secrets work](how-secrets-work.md)
