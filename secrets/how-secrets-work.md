# How Secrets Work

Secrets are environment variables that Amezmo encrypts in your browser before it
saves them, so the plaintext value never reaches Amezmo. Use them for API keys,
license keys and other sensitive strings you don't want in source control or in
your ``.env``.

When you save a secret, your browser seals the value with your instance's public
key and sends only the sealed value. Your instance decrypts it in memory using a
private key in the instance's home directory, which Amezmo can't read.
When you terminate an instance, that private key is destroyed and never reused.

## When Secret Changes Apply

Secrets are read during deployment, not while your app is running. Adding,
changing or deleting a secret takes effect on your next deployment, so trigger a
deployment to apply it. This is different from
[environment variables](../configuration/dotenv.md), which apply as soon as you
save them.

There is no edit action for a secret. To change one, delete it and add it again
with the new value, then deploy.

## Secrets and the .env File

Secrets are not written to your ``.env`` file. Amezmo injects them into your
[deployment hooks](../deployments/hooks/index.md), so a hook script can read a
secret while it runs. Your running app reads its values from ``.env``, which is
a separate place. See [environment variables](../configuration/dotenv.md).
