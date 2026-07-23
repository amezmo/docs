# Tag-based deployments

Instead of using a static branch name for automatic deployments, you may create a tag based deployment rule.
With tag-based Git deployments, you define one or more tag patterns using regular expressions. To learn more about setting tag patterns on your environment, 
see the [Update Environment](../api/environments/update-environment.md) API endpoint.

## Tag patterns
A tag pattern is a regular expression string. Tag patterns define a dynamic pattern-based rule for automatic deployments.
When one or more tag pattern is defined in your environment, the tag-based regular expression rules take precedence over 
your static [automatic deployment branch](branches.md). 

## How tag-based deployments work
When a tag is created in your [git repository](repos.md),
Amezmo receives a webhook event from your Git provider. Within the event payload, a git reference is defined. 
A [git reference](https://git-scm.com/book/en/v2/Git-Internals-Git-References), or git ref is either a commit ID, or a tag. 
Both commit IDs and tags are strings and are associated with a ref type. The value of a git reference type is either "branch", or "tag".

Amezmo gets an event for when a tag is created and then loops through your list of regular expression patterns and performs a 
match against the tag name. If a match is found, the deployment is executed, and no more matches are attempted. To see the value of your environment's
tag patterns, see the `auto_deploy_tag_patterns` property within the [Get an environment](../api/environments/get-environment.md) API endpoint.


## Resources
- [List environments](../api/environments/list-environments.md)
- [`auto_deploy_tag_patterns`](../api/environments/update-environment.md#parameters)