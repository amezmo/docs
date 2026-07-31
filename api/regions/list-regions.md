# List regions

{.lead}
List every **region** where you can launch an instance. Each region has an id
you pass to [Create an instance](../instances/create-instance.md), along with
its name and ISO country code.

`GET` /v1/regions

## Code samples for "List regions"

### Request example

{title="GET /v1/regions"}
```bash
curl https://api.amezmo.com/v1/regions \
    -H "Authorization: Bearer $AMEZMO_API_KEY"
```

### Response

The response is an array of regions. Retrieve one region with
[Get a region](get-region.md).

{title="200 OK"}
```javascript
[
    {
        "id": "lb2-us",
        "iso_country_code": "US",
        "name": "United States"
    },
    {
        "id": "au2-au",
        "iso_country_code": "AU",
        "name": "Australia"
    },
    {
        "id": "uk3-uk",
        "iso_country_code": "UK",
        "name": "United Kingdom"
    },
    {
        "id": "ca-ca",
        "iso_country_code": "CA",
        "name": "Canada"
    }
]
```
