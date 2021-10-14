# Deployments

You may begin a new deployment on Amezmo without using Git. To deploy without Git, you must supply an archive file in the form of a .zip file. This archive should contain the full source code of your application.
Archive deployments support both staging and production environments.

- `GET` [Get a deployment](/docs/api/deployments/get)
- `POST` [Create a deployment](/docs/api/deployments/post)
- `POST` [Cancel a deployment](/docs/api/deployments/cancel-deployment)

## How-to Guides

- [How to create a ZIP archive for API deployments](/docs/how-to-guides/creating-zip-files-for-api-deployments)
- [How to deploy a ZIP archive using Amezmo](/laravel-hosting-guides/deploying-laravel-with-github-actions#deploy-job-deploying-to-amezmo-using-amezmo-api)
