# Get a deployment

```http
GET /v1/instances/{instance_id}/deployments/{deployment_id}
```

## Parameters

Parameter     |  Type  | In    | Description
------------- | -------|------ |------------------
instance_id   | string | uri   | The instance id of the environment
deployment_id | string | uri   | The deployment ID

## Response

`200 OK`

```json
{
    "id": 838,
    "status": "cancelled"
}
```
