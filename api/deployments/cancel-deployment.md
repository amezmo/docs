# Cancel Deployment

`POST` /v1/deployments/{deployment_id}/cancel

## Parameters
Parameter     |  Description       
------------- | ------------- 
deployment_id | The deployment ID

## Response

`200 OK`

```bash
{
    "id": 838,
    "status": "cancelling"
}
```