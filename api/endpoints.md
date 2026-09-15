# API Endpoints

{.lead}
The Amezmo **API** is a REST API with a single base URL. Every request
authenticates with a Bearer token and returns JSON.

{title="API base URL"}
```bash
https://api.amezmo.com/v1
```

The `/v1` prefix versions the API, so a later version can ship without breaking
existing integrations. You send parameters as form fields and receive JSON in
the response.

## Authentication

Every request needs a Bearer token. Your API key is in the dashboard under
**Profile > API keys**. You send it in the `Authorization` header. See
[Authentication](authentication/index.md) for more detail.

The examples below read the key from an `AMEZMO_API_KEY` environment variable,
so you set it once instead of pasting it into every command:

{title="Set your API key"}
```bash
export AMEZMO_API_KEY="your-api-key"
```

## Errors

A failing request returns a JSON body with the same fields every time: a `type`
to branch on, a specific `code`, a human `message`, and a `request_id` to quote
when you report a problem. See [Errors](errors.md).

{title="404 Not Found"}
```javascript
{
    "http_status": 404,
    "type": "invalid_request_error",
    "code": "unknown_resource_error",
    "message": "The requested resource does not exist or you do not have permission to access it.",
    "errors": {},
    "doc_url": "https://www.amezmo.com/docs/api",
    "request_id": "req_01HZX9C4Q2",
    "error": null
}
```

## Example Request

This request lists the regions where you can launch an instance. The double
quotes let the shell substitute your key into the header:

{title="GET /v1/regions"}
```bash
curl https://api.amezmo.com/v1/regions \
    -H "Authorization: Bearer $AMEZMO_API_KEY"
```
