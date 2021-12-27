Locker
======

The Kenshi locker can be used to lock any BEP-20 tokens for a set period of time.
For example, you can use it to lock your liquidity tokens or use it to lock up
your team allocations for as long as your project requires.

Features
--------

Kenshi lockers have a set of features that makes them stand out in the competition:

- **One time flat fee**: pay one time and use forever, do whatever.
- **Upgradable**: upgrade your locker to a new version for free any time we add new features.
- **Lock any token**: lock any token on the Binance Smart Chain.
- **Lock multiple tokens**: lock multiple tokens or lp tokens in the same locker.
- **Transfer ownership**: transfer ownership to a new wallet if needed.

Pricing
-------

Kenshi lockers have a one time flat fee and all future interactions with them
are free. Locker costs are payable either in BNB or in Kenshi. Please note that
paying in Kenshi gives you a ~50% discount compared to the BNB price, and you
won't pay the Kenshi sales tax.

.. list-table:: Pricing
   :widths: 60 20 20
   :header-rows: 1

   * - Locker Action
     - Price (BNB)
     - Price (Kenshi)
   * - Create a new locker
     - 0.2
     - 1,000,000,000
   * - Lock liquidity or other tokens
     - *Free*
     - *Free*
   * - Increase locked liquidity or other tokens
     - *Free*
     - *Free*
   * - Increase lock time
     - *Free*
     - *Free*
   * - Transfer ownership
     - *Free*
     - *Free*
   * - Upgrade to a new locker version
     - *Free*
     - *Free*

How to create a locker?
-----------------------

To create a locker, go to the `/locker`_ page on our website, connect your wallet
and click on the create button. Once the locker creation is done you will be
redirected to the admin page. Be sure to copy the contract address of your newly
created locker so you can manage it later.

.. _`/locker`: https://kenshi.io/locker

How to add tokens to the locker?
--------------------------------

You can either use the admin page of the locker for sending tokens into the locker,
or you can simply send tokens to the locker contract address from the wallet of
your choice.

.. danger::

  When sending tokens to the contract address, make sure you're on the correct
  network. Otherwise your tokens will be lost forever.

How to withdraw tokens from the locker?
---------------------------------------

Go on the admin page of your locker, connect with your wallet, enter the address of
the token you want to remove in the **Lock / Withdraw** section, click on the **Withdraw**
button.

How to lock the tokens?
-----------------------

Go to the admin page of your locker, connect your wallet, choose a date and click
on the **Change** button. If you want to extend the lock time you can do it the same
way.

How do I see details about a locker?
------------------------------------

You can go on to the locker's admin page, connect your wallet and see the information
publicly available on the locker.

.. note::
  
  Admin actions such as locking, withdrawing and setting the dates are only available
  and displayed to the locker owner. Locker onwer is anyone who created the locker.
  Please not that the ownership of the locker is not transferrable.


Programmatic access
-------------------

Check our `GitHub repository`_ for the relevant interfaces and documentation.

.. _`GitHub repository`: https://github.com/kenshi-token/locker-interface
