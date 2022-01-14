# Encryption

Backups can
be automatically encrypted using the industry standard AES-256 encryption algorithm with a SHA256 message digest
when you set an encryption key in the Database settings section.
Amezmo uses OpenSSL to encrypt your backups.

## Recommended decryption command
The following command is the recommended way to portably decrypt your backup files. After downloading your backup
file, this command should be run on your local machine.

```bash
openssl enc -aes-256-cbc -md sha256 -d -pass pass:$KEY \
    -in $BACKUP_FILE | gzip -d
```