# Hourly billing overview

You are billed on an hourly basis for each instance you launch on Amezmo. Although you will always see monthly
pricing on the Amezmo page, you are always billed hourly "behind the scenes." This feature has several advantages:

## Billing periods
Your card is charged on the first day of the month for every hour that you had an active [instance](/docs/instances) during the **prior** month. For example,  Let's say you launched a single instance on Amezmo for the first time on July 6th. With this example, you will be billed on August 1st for all usage between the period July 6th - July 31st.

## Usage
"Usage" is defined as a unit of 60 minutes (1 hour) that an [instance](/docs/instances) is active. 
An active instance is defined as an instance that was launched, but not terminated (deleted). An instance becomes *inactive* after [terminating](/docs/instances/terminating) it. On Amezmo, you are charged hourly, for each active instance. 

## Organized invoices
Always pay for your services on the first of every month, never in the middle of the month, or sparsely
throughout the month.

## Pay for what you use
If you only use an instance, for example, to test out a new PHP application, then you don’t have to pay
for a full month of service if you only require the instance for a few days.

## How it works

If you terminate an instance, you will only pay for the total number of hours the instance was active during the
month. Let's go through an example. Alice launches an instance on January 6th, 2021. She then
imports a fresh application to test a new client project.

Unfortunately, her client informs her on January 9th, 2021 that they need to cancel the project. In turn,
Alice terminates the application on Amezmo and bills the client.
The total bill for Alice's usage on Amezmo for this client project would be for only 3 days, not a full month.

To calculate the total price, take the instance type and divide it by 744.
744 is the optimistic number of hours in a full month during a calendar year.
Since there are only ever a maximum of 31 days per month (and often less than that), 744 hours is the maximum
number of hours you're billed for during any given month. But it’s less than this during the months of
February, April, June, July, September, October, and November.

## Hours per month
Month     | Hours
----------|--------
January   | 744
February  | 672
March     | 744
April     | 720
May       | 744
June      | 720
July      | 744
August    | 744
September | 720
October   | 744
November  | 720
December  | 744

