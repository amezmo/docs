# Scaling

Amezmo provides the ability for you to upgrade your instance configuration at anytime.
Upgrades can be necessary for times when you need more memory, or computing power.

You can also downgrade your instance
to a lower instance configuration. This can be useful for when you do not need the computing power offered by a higher instance
type.

## How to upgrade/downgrade

Upgrading or downgrading your instance can be done in one click. Upgrade by going to the Overview page.
Once you've decided which instance type you'd like to have, click the blue "Next" button.

![Upgrade your instance](https://s3.us-east-2.amazonaws.com/static.amezmo.net/Upgrade.png){.img-enlargable}


After you've chosen your desired instance type and have clicked the button, you'll be prompted for confirmation.
Click the blue "Upgrade/Downgrade Instance"  button, and your instance will be queued for reformation.

![Confirm instance upgrade](https://s3.us-east-2.amazonaws.com/static.amezmo.net/ConfirmUpgrade.png){.img-enlargable}

## FAQ

<details>
<summary>Will I be charged for upgrading?</summary>

If your instance is upgraded to a higher tier, you will be charged the price difference between your current instance,
and your new instance price.

</details>

<details>
<summary>How long does it take to upgrade/downgrade?</summary>

Upgrading or downgrading your instance happens asynchronously. Your upgrade request will be queued as a job to the Amezmo
worker process, which will then handle the instance resize.

</details>

<details>
<summary>Will upgrading to a bigger server configuration require downtime?</summary>

In some cases, yes, but Amezmo will prompt you with a confirmation if downtime will be required. A small amount of downtime
is required if the instance is being changed to a smaller instance type.

</details>
