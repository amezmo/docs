# Turn off NPM package caching

You can disable [NPM package caching](/docs/npm/package-caching) if you're running into problems
with symbolic links, or for other reasons such as wanting to ensure that `node_modules` is built from
scratch on every deployment.

## Disable NPM package caching
- Open the Amezmo dashboard at [https://www.amezmo.com/sites](/sites)
- Choose the name of the application.
- Above the horizontal tab navigation menu, click the Production **or** Staging tab.
- In the horizontal tab navigation menu, choose the **Deployments** tab.
- Scroll down to the **Settings** section.
- Find the NPM toggle switch.
    
    <img class="img-enlargable" src="https://s3.us-east-2.amazonaws.com/static.amezmo.net/npm-caching.png" />
- Click the switch

After turning off NPM package caching, your next deployment will not use the cached
`node_modules` directory.
