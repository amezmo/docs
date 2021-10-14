# Creating ZIP files for API deployments

You can deploy your application via the Amezmo API using an archive file such as ZIP. In this guide, you will
create a ZIP file for [API deployments](/docs/api/deployments/post). The specific command allows
the ZIP file to be created without a parent directory.

## Create a ZIP file from the command line

This command **includes** hidden files such as `.git`

```bash
    cd my-application;
    zip --recurse-paths ../my-application.zip .
```

## Create a ZIP file from the command line excluding the Git directory
```bash
    cd my-application;
    zip -x \*.git\* --recurse-paths ../my-application.zip .
```

## See also
- [Amezmo API Docs](/docs/api)
