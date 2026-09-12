# Amezmo REST API

The Amezmo API gives you programmatic access to Amezmo which empowers you to create deployments,
launch instances, and manage resources.

## Getting Started

### API Endpoint

A REST API with a single base URL, `https://api.amezmo.com/v1`, returning JSON.
Start with the [API endpoint](endpoints.md) reference for the base URL and
request format.

### Authentication

Every request carries a Bearer token. [API authentication](authentication/index.md)
covers where to find your key and how the examples store it in an
`AMEZMO_API_KEY` environment variable.

### Errors

Every failure returns the same JSON body. [Errors](errors.md) documents that
envelope, the error types worth branching on, and the codes behind them.

## Core Resources

### Workers

Start, stop, and restart [worker processes](workers/index.md) through the API.

### Instances

Your applications, along with their environments and resources.
[Instance endpoints](instances/index.md) list and get instances, list instance
types, and terminate an instance.

### Environments

An environment ties an instance to a Git repository and its deployment rules.
[Environment endpoints](environments/index.md) list, get, and update those,
including automatic deployment settings.

### Deployments

Deploy without Git by supplying a `.zip` archive of your source.
[Deployment endpoints](deployments/index.md) create, get, and cancel
deployments in both staging and production.

### Cron

List, get, create, and update the [cron entries](cron/index.md) on an
instance.

### Regions

[Region endpoints](regions/index.md) list the regions an instance can run in
and get a single region.
