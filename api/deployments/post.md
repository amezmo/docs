# Create a deployment

You may invoke a deployment on your instance with an optional archive file. This archive file allows you to
upload a complete version of your application without having to use Git. A common use case for deploying with an archive file is when you're using a pipeline provider such as GitHub actions.

Deployments with an archive file work exactly
like Git deployments, but they don't have any commit information associated with them.

When deploying with the Amezmo API, The `after.pull` 
[deployment hook](/docs/deployments/hooks) will not be run.
Instead, use the [after.extract](/docs/deployments/hooks/after-extract) hook to run code after extracting your archive. 

`POST` /api/sites/{site_id}/deployments

## Parameters

Parameter     |  Description       
------------- | ------------- 
api_key       | Your [API key](/docs/api/authentication).
environment   | The [environment](/docs/environments) for this deployment. This can be `production` or `staging`.
site_id       | The ID of the instance that this deployment will be executed on.
archive       | The archive file that contains the source code of your application. This can be a zip or a tar archive. The maximum size of an archive file is 512MB.


## Code samples

```bash
curl --request POST \
    --url https://api.amezmo.com/api/sites/{site_id}/deployments \
    --header 'Authorization: Bearer {api_key}' \
    --header 'Content-Type: multipart/form-data' \
    --form environment=production \
    --form archive=@{archive}
```

## Response

`201` Created

```bash
{
    "id": 838,
    "status": "pending"
}
```

## Resources
- [How to create a ZIP archive for API deployments](/docs/how-to-guides/creating-zip-files-for-api-deployments)

