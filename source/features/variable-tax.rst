Variable Tax
============

Since Kenshi is an investment token, holders promise to hold onto their
tokens for at least 30 days, otherwise they will face a fine. This fine
is added to the `5% base tax`_ to make up the variable tax rates.
The fine is calculated logarithmically with the amount decreasing as
we move further away from the date of purchase.

.. _`5% base tax`: ../tokenomics.html#tax

Why is this good?
-----------------

In an automated market maker (AMM), every purchase increases the price of the
token, and every sale decreases its price. This makes tokens vulnerable to market
manipulations. For example, groups of people can buy the token at a low price,
creating a hype to pump the price, then sell all their tokens at that high price
for profit, thus crashing the market for all the other holders.
This is called a pump and dump scheme.

The variable tax system helps prevent these scenarios of market manipulation
from happening, ensuring the savings of the holders stay safe.

How much is the fine?
---------------------

A fine is added to the base tax when an early sale happens. Check the chart
below for the value of the fine based on how many days passed from the
date of purchase:

.. chart:: ../_static/charts/tax.json

