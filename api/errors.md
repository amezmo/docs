# Errors

{.lead}
Every Amezmo API error returns the same JSON body, whatever went wrong. Branch on
`type` to decide how to handle it and on `code` when you need the exact reason.

{title="422 Unprocessable Entity"}
```javascript
{
    "http_status": 422,
    "type": "invalid_request_error",
    "code": "validation_error",
    "message": "The request you provided failed validation.",
    "errors": {
        "expression": "This is an invalid cron expression."
    },
    "doc_url": "https://www.amezmo.com/docs/api/cron/update-cron-entry",
    "request_id": "req_01HZX9C4Q2",
    "error": null
}
```

Field        | Description
------------ | -----------------------------------------------------------------
`http_status`| The HTTP status, repeated in the body so it survives logging
`type`       | The coarse class of error. A short, closed set, listed below
`code`       | The specific reason. Open-ended, so treat an unfamiliar one as its `type`
`message`    | A human-readable explanation. Not a stable interface: don't match on it
`errors`     | Per-parameter messages, keyed by parameter name. `{}` when not a validation failure
`doc_url`    | The reference page for whatever failed
`request_id` | Identifies this request. Quote it when you contact support
`error`      | Debugging detail, always `null` outside development

## Types

`invalid_request_error`
: Something about the request is wrong: a bad parameter, a resource that doesn't
exist, a state that forbids the action, or an unmet account requirement. Retrying
the same request unchanged fails the same way.

`authentication_error`
: Your API key is missing, malformed, disabled, or not allowed to do this. See
[Authentication](authentication/index.md).

`rate_limit_error`
: You sent too many requests. Back off and retry.

`api_error`
: Something failed on Amezmo's side. These are safe to retry.

## Codes

The codes you're most likely to handle. Individual endpoints add their own for
situations only they can hit, documented on that endpoint's page. New codes get
added as the API grows, so treat an unrecognized one as its `type` rather than
failing.

Code                         | Status | Meaning
---------------------------- | ------ | -------------------------------------------
`validation_error`           | 422    | One or more parameters failed validation. See `errors`
`unknown_resource_error`     | 404    | No such resource, or your key can't see it
`method_not_allowed`         | 405    | Wrong HTTP method for this path
`conflict`                   | 409    | The resource's current state forbids this
`unauthenticated`            | 401    | No usable API key on the request
`invalid_credentials`        | 401    | The API key was rejected
`forbidden`                  | 403    | The key is valid but not allowed to do this
`email_verification_required`| 403    | Verify your email address first
`payment_method_required`    | 402    | Add a payment method first
`payment_method_flagged`     | 402    | Your payment method could not be verified
`account_past_due`           | 402    | Settle an outstanding balance first
`feature_not_supported`      | 422    | Your instance type doesn't include this feature
`invalid_instance_state`     | 409    | The environment is paused, launching, or failed
`instance_in_progress`       | 422    | Another instance is still being created
`instance_limit_reached`     | 422    | You're at your account's instance limit
`rate_limit_exceeded`        | 429    | Too many requests
`internal_error`             | 500    | Something failed on Amezmo's side

## Validation errors

A `validation_error` fills in `errors` with one message per rejected parameter,
keyed by the parameter's name. Everything else leaves `errors` as `{}`.

{title="Reading a validation failure"}
```bash
$ curl -s https://api.amezmo.com/v1/instances/{instance_id}/cron/412 \
    -X PATCH \
    -H "Authorization: Bearer $AMEZMO_API_KEY" \
    --data-urlencode expression='every other tuesday' \
    | python3 -c 'import json,sys; print(json.load(sys.stdin)["errors"])'
```

## Reporting a problem

`request_id` identifies one request on Amezmo's side. Include it when you write
to [support](../support/index.md), along with the endpoint and roughly when you
called it.
