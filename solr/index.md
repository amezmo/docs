# Solr

The Solr full-text search platform is provided for Drupal applications. Amezmo provides
this with the Advanced instance type. See below for some resources for getting started.

## Solr API

From your [SSH](/docs/instances/ssh) session, you can check which cores are created with
this command

```curl
curl http://localhost:${SOLR_PORT:-8983}/solr/admin/cores
curl http://localhost:8983/solr/drupal/config
curl http://localhost:8983/solr/drupal/schema
```

## Resources

- [Solr configuration](/docs/solr/configuration)
- [Solr Reference](https://solr.apache.org/guide/solr/latest/configuration-guide/config-api.html)