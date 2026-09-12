# Get a region

{.lead}
Get a single **region** by its id, including its name and ISO country code.
Use it to confirm a region before you launch an instance there.

`GET` /v1/regions/{region_id}

## Parameters

Parameter | Type   | In  | Required | Description
--------- | ------ | --- | -------- | --------------------------------------------------
region_id | string | uri | Yes      | The region id. See [List regions](list-regions.md)

## Code samples

### Request example

{title="GET /v1/regions/{region_id}"}
```bash
curl https://api.amezmo.com/v1/regions/au2-au \
    -H "Authorization: Bearer $AMEZMO_API_KEY"
```

### Response

{title="200 OK"}
```javascript
{
    "id": "au2-au",
    "iso_country_code": "AU",
    "name": "Australia"
}
```
