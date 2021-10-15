# Create a deployment

You may invoke a deployment on your instance with an optional archive file. This archive file allows you to
upload a complete version of your application without having to use Git. A common use case for deploying with an archive file is when you're using a pipeline provider such as GitHub actions. 

See the [Amezmo GitHub Actions](https://github.com/amezmo/github-actions-demo) repository for a complete working example of using GitHub actions to deploy an application.

Deployments with an [archive file](/docs/how-to-guides/creating-zip-files-for-api-deployments) work exactly
like regular Git deployments.

When deploying with the Amezmo API, The `after.pull` 
[deployment hook](/docs/deployments/hooks) will not be run.
Instead, use the [after.extract](/docs/deployments/hooks/after-extract) hook to run code after extracting your archive. 

```bash
POST /api/sites/{site_id}/deployments
```

## Parameters

Parameter      |  Type | In | Description       
-------------  | ------------- 
api_key        | string  | header | **Required**. Your [API key](/docs/api/authentication).
environment    | string  | body | **Required**. The [environment](/docs/environments) for this deployment. This can be `production` or `staging`.
site_id        | integer | uri | **Required**. The ID of the instance that this deployment will be executed on.
archive        | body    | uri | **Required**. The archive file that contains the source code of your application. This can be a zip or a tar archive. The maximum size of an archive file is 512MB.
repo_owner     | string | body | The repository owner. Required if `repo_name` is provided.
repo_name      | string | body | The repository name. Required if `repo_owner` is provided.
branch         | string | body | The name of the branch
pusher         | string | body | The email address of the user that invoked the deployment
commit         | string | body | The git commit hash
tag            | string | body | The git tag


## Code samples

```bash
curl --request POST \
    --url https://api.amezmo.com/api/sites/{site_id}/deployments \
    --header 'Authorization: Bearer {api_key}' \
    --header 'Content-Type: multipart/form-data' \
    --form environment=production \
    --form archive=@{archive} \
    --form repo_owner=amezmo \
    --form repo_name=github-actions-demo \
    --form branch=main \
    --form pusher=me@example.com

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

