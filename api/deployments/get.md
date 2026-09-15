# Get a deployment

{title="GET /v1/instances/{instance_id}/deployments/{deployment_id}"}
```http
GET /v1/instances/{instance_id}/deployments/{deployment_id}
```

## Parameters

Parameter     | Type   | In  | Required | Description
------------- | ------ | --- | -------- | ----------------------------------
instance_id   | string | uri | Yes      | The instance id of the environment
deployment_id | string | uri | Yes      | The deployment ID

## Response

`200 OK`

{title="200 OK"}
```json
{
    "id": 838,
    "status": "cancelled"
}
```
