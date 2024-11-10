# Cancel Deployment

```http
POST /v1/instances/{instance_id}/deployments/{deployment_id}/cancel
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
    "status": "cancelling"
}
```
