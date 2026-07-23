# Metrics

The Metrics tab shows how your environment is performing: CPU, memory and HTTP
request stats for the environment you're viewing.

## CPU

The percentage of your plan's allocated CPU in use, averaged over five minutes.
At 100% the environment is using its full CPU allotment.

## Memory

The percentage of your environment's memory limit in use.

## HTTP Requests

The total number of requests over the selected window, with a breakdown of 2xx,
4xx and 5xx responses and each one's share of the total. Amezmo measures this at
the load balancer. There's no response-time metric here.

## Time Ranges

CPU and Memory each have a time-range menu: 1 minute, 5 minutes, 30 minutes, 1
hour, 6 hours, 12 hours, 24 hours and 1 week. Plans with 30-day retention also
get a 30-day option. The default is the last 30 minutes, and your choice is
remembered.

## Alerts

From the CPU and Memory panels you can set an alert that emails you when usage
crosses a threshold you choose.
