# Changing the default Composer version

You can change the default Composer version that is used for
your automatic deployments.

## How to change the default Composer version

1. Open the Amezmo dashboard at [https://www.amezmo.com/sites](/sites)
2. Choose the name of the application.
3. Above the horizontal tab navigation menu, click the Production **or** Staging tab.
4. In the horizontal tab navigation menu, choose the **Deployments** tab.
5. Scroll down to the **Settings** section.
6. Find the "Composer packages" switch.
    <img class="img-enlargable" src="https://s3.us-east-2.amazonaws.com/static.amezmo.net/composer-settings-switch.png" />
7. Click the **Settings** button on the far right
8. Choose your desired Composer version from the dropdown
9. Click **Save**


After changing the default Composer version, [composer](/docs/deployments/automatic-composer-installs), the version you selected is available
in your [deployment hooks](/docs/deployments/hooks).
