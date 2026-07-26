# API changelog

The changelog lists forward-compatible changes to the API.

## 2022-12-12

**Added**

- `current_deployment` to [Get Environment](environments/get-environment.md)

## 2022-04-18

**Added**

- `ssh_enabled` and `trusted_ssh_ips` parameters to [Update Environments](environments/update-environment.md). In addition to accepting these parameters in the PUT
request, they are also shown in the [Get an environment](environments/get-environment.md) resource.

## 2022-01-19

**Added**

- `newrelic_license_key` parameter to [Update Environments](environments/update-environment.md)

## 2020-10-14

**Added**

- New optional request properties to [Deployments](deployments/post.md)
