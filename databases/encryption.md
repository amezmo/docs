# Database backup encryption

Backups can
be automatically encrypted using the industry standard AES-256 encryption algorithm with a SHA256 message digest
when you set an encryption key in the Databases > Automation settings section.
Amezmo uses OpenSSL to encrypt your database backup files.

When an encryption key is provided, the value is encrypted at rest using your instance's private key. The value that you provide is encrypted in 
the same way that [Secrets](/docs/secrets) are encrypted.

## Recommended decryption command
The following command is the recommended way to portably decrypt your backup files. After downloading your backup
file, this command should be run on your local machine.

```bash
openssl enc -aes-256-cbc -md sha256 -d -pass pass:$KEY \
    -in $BACKUP_FILE | gzip -d
```
