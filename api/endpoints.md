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

## Example Request

This request lists the regions where you can launch an instance. The double
quotes let the shell substitute your key into the header:

{title="GET /v1/regions"}
```bash
curl https://api.amezmo.com/v1/regions \
    -H "Authorization: Bearer $AMEZMO_API_KEY"
```
