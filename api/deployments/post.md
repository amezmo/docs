# Create a deployment

You may invoke a deployment on your instance with an optional archive file.
This archive file allows you to upload a complete version of your
application without having to use Git.

A common use case for deploying with an archive file is when
you're using a pipeline provider such as GitHub actions.

See the [Amezmo GitHub Actions](https://github.com/amezmo/github-actions-demo) demo
repository for a guide to Deploying PHP applications
with [GitHub actions](https://www.amezmo.com/laravel-hosting-guides/deploying-laravel-with-github-actions).

Deployments with an [archive file](../../how-to-guides/creating-zip-files-for-api-deployments.md) work exactly
like regular Git deployments.

When deploying with the Amezmo API, The `after.pull`
[deployment hook](../../deployments/hooks/index.md) will not be run.
Instead, use the [after.extract](../../deployments/hooks/after-extract.md)
hook to run code after extracting your archive.

{title="POST /v1/instances/{instance_id}/deployments"}
```http
POST /v1/instances/{instance_id}/deployments
```

## Parameters

Parameter   | Type   | In     | Required    | Description
----------- | ------ | ------ | ----------- | -----------------------------------------------------------------------------------------------------------------------------------------------------
api_key     | string | header | Yes         | Your [API key](../authentication/index.md).
environment | string | body   | Yes         | The [environment](../environments/index.md) name for this deployment. This can be `production` or `staging`.
instance_id | string | uri    | Yes         | The ID of the instance that this deployment will be executed on.
archive     | file   | body   | Yes         | The archive file that contains the source code of your application. This can be a zip or a tar archive. The maximum size of an archive file is 512MB.
repo_owner  | string | body   | Conditional | The repository owner. Required if `repo_name` is provided.
repo_name   | string | body   | Conditional | The repository name. Required if `repo_owner` is provided.
branch      | string | body   | No          | The name of the branch
pusher      | string | body   | No          | The email address of the user that invoked the deployment
commit      | string | body   | No          | The git commit hash
tag         | string | body   | No          | The git tag

## Code samples

{title="cURL request example"}
```curl
curl --request POST \
    --url https://api.amezmo.com/v1/instances/{instance_id}/deployments \
    --header "Authorization: Bearer $AMEZMO_API_KEY" \
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

{title="201 Created"}
```json
{
    "id": 838,
    "status": "pending"
}
```

## Resources

- [How to create a ZIP archive for API deployments](../../how-to-guides/creating-zip-files-for-api-deployments.md)
