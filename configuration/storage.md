# Persistent storage

The `/webroot/storage` directory is available for your persistent storage needs. By default,
this directory is created for you when you launch an instance. You should configure your application to
write files to this directory if you need to persist user uploaded content, or other files across deployments.

## Directory layout
```bash
/webroot
    |----logs
    |----storage
    |-------public
    |----current -> /webroot/release/${TIMESTAMP}.${COMMIT_ID}
    |----release
    |-------${TIMESTAMP}.${COMMIT_ID}
    |-------${TIMESTAMP}.${COMMIT_ID}
```

By default, `/webroot/storage` is owned by user `deployer` and group `www-data`.
All files and directories written to `/webroot/storage` will inherit the group of`www-data`.

As part of the deployment process, Amezmo will run a chmod across your target deployment directory. This ensures that
any files created from your hooks will have correct and expected permissions. Amezmo ensures the owner/group is
`www-data:deployer`. This allows for expected permissions across all areas of your application.

The `/webroot/storage/public` is created for [public file uploads](/docs/configuration/public-directory). Files uploaded to
this directory can be accessible from your domain by creating a symbolic link
from  `/webroot/storage/public` to `/webroot/current/public`. See the [public directory documentation](/docs/configuration/public-directory) for more details.

When uploading files from your PHP app, the default owner and group is `www-data`. At this time,
Amezmo has chosen not to modify the default PHP FPM configuration in an effort to run
the FPM daemon as a non-shell capable access user. We recommend the following file system permissions when
writing and uploading new files to your instance.


## Recommend file permissions settings

The following permission configuration is Amezmo's recommendation for PHP applications hosted on Amezmo. Note that
the example shows a Laravel based configuration array, but these permissions are not specific to Laravel. Any PHP
application hosted on Amezmo should use these permissions and settings.


This file is located at `app/config/filesystems.php`. The

```php
return [
    // Other code omitted
    'default' => 'public',
    'disks' => [
        'local' => [
            'driver' => 'local',
            'root' => '/webroot/storage',
            'permissions' => [
                'file' => [
                    'public' => 0664,
                    'private' => 0664,
                ],
                'dir' => [
                    'public' => 0700,
                    'private' => 0700,
                ],
            ],
        ],

        'public' => [
            'driver' => 'local',
            'root' => '/webroot/storage/public',
            'url' => env('APP_URL').'/storage',
            'visibility' => 'public',
            'permissions' => [
                'file' => [
                    'public' => 0664,
                    'private' => 0664,
                ],
                'dir' => [
                    'public' => 0700,
                    'private' => 0700,
                ],
            ],
        ],
    ],
];
```

The above permissions provide expected behavior across all application areas. With the above file permissions,
your depoyment hooks may read and write existing and new files and your workers may read and write existing
and new files.

## Resources
- [How to Persist Storage Across PHP Deployments on Amezmo Part 1](https://www.youtube.com/watch?v=A-iBIfch6Bw)  <span class="badge bg-info">Video</span>
- [How to Change the Default Storage Path in Laravel](https://www.amezmo.com/blog/how-to-change-the-default-storage-path-in-laravel/)
- [Laravel deployment hook for persistent storage](https://github.com/amezmo/demo.amezmo.com/blob/master/.amezmo/before.deploy)

