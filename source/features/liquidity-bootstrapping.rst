Liquidity Bootstrapping
=======================

.. warning::
  Please make sure you completely understand this section
  before buying any Kenshi tokens.

The Kenshi liquidity pool on PancakeSwap differs a little bit from other
liquidity pools on the same DEX. We have added a functionality similar to
what the Balancer LBP does, but we've implented it off-chain, and on top
of the existing PancakeSwap liquidity pools.

This allows us to have a higher price for the token at the start, and
have a bigger liquidity in the pool over time, which in turn helps us
stabilize and control the price.

This feature is implented off-chain because we couldn't fine any currently
existing DEX on the Binance Smart Chain offering a similar service. We will
have this feature on our own DEX once we launch the Kenshi DEX project.

How does it work?
-----------------

At IDO, we pair 10% of our tokens with a specific amount of BNBs. This
defines the inital price of the token. The 90% of the remaining tokens are
locked in the smart contract.

Every time a trade happens and removes some tokens from the liquidity pool,
an oracle reacts to the event by injecting the same amount of tokens back to
the pool to keep the amount of Kenshi tokens in the pool a constant.

This process continues until all the 90% of the remaining tokens are injected
into the pool. The price impact of this process is rather small, and guarantees
an overall positive trend for the price.

Once all tokens are injected into the pool, the token price goes up at a normal
rate, just like any other token. This whole process can be viewed as a purchase
tax where a small fraction of the BNBs used for a purchase are used to *balance*
one side of the liquidity pool in favor of the other.

.. note::
  Interested in purchasing this oracle for your own token? Use `this form`_ to
  submit a request, we'll contact you as soon as possible.

You can check out the documentation for our `Liquidity Bootstrapping Oracle`_
if you want to learn more about this.

.. _`this form`: https://kenshi.io/liquidity-bootstrapping
.. _`Liquidity Bootstrapping Oracle`: ../services/lbp.html
