# API Authentication

The Amezmo API authenticates each request with your API key. Your API key is in
the dashboard under **Profile > API keys**.

The examples store the key in an `AMEZMO_API_KEY` environment variable, so you
set it once and reuse it:

{title="Set your API key"}
```bash
export AMEZMO_API_KEY="your-api-key"
```

You send the key as a Bearer token in the `Authorization` header. The double
quotes let the shell substitute your key:

{title="Authorization header"}
```bash
-H "Authorization: Bearer $AMEZMO_API_KEY"
```