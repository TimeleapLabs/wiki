Kenshi Token Price
==================

This article explains all the factors involved in the pricing of Kenshi
tokens, and proposes a few ways you can help increase the price. We will
start with the basics, if you're familiar with any of the concepts in each
section, you can just skip to the next.

Automated Market Maker
----------------------

Kenshi tokens are sold on PancakeSwap_. PancakeSwap is a decentralized
exchange (DEX) that uses automated market maker (AMM) protocol for trading
the tokens. When listing on an AMM, it is required to make a liquidity pool.
In simplest form, a liquidity pool is just a pair of tokens that are traded
against each other.

The formula used by an AMM is very simple. In an AMM, for a pair of token X
and token Y, the following formula should always hold:

.. math::
  X \times Y = Constant

An example of this would be the Kenshi / BUSD pair on PancakeSwap. Deploying
1000 Kenshi tokens against 10 BUSD, leads to the following constant:

.. math::
  1000 \times 10 = 10000

The price of the token is defined based on the same formula. Let's say you
want to buy 50 Kenshi tokens, that means you are going to remove
that amount of Kenshi tokens from the liquidity pool, and in return you are
adding B amount of BUSD tokens to the pool, we'll then have:

.. math::
  (1000 - 50) \times (10 + B) = 10000

Solving the above equation for B gives us the price of 10 Kenshi tokens
at the time of trade:

.. math::
  B = \dfrac{10000}{1000 - 50} - 10 \approx 0.526

It means to buy 10 Kenshis, you'll need to pay 0.526 BUSDs. After making the
purchase, the amount of tokens in the pool changes to 950 Kenshis and 10.526 BUSDs.
Let's say some other person arrives now, and wants to buy 50 Kenshis as well.
Do they have to pay the same amount of BUSD in order to get this amount of Kenshis?
Let's recalculate:

.. math::
  (950 - 50) \times (10.526 + B) = 10000

.. math::
  B \approx	0.585

As you can see, now the price of the token is more than before. Basically, the more
Kenshi that is bought and removed from the pool the more BUSDs will be in the pool,
making the price of Kenshi tokens go higher.

It works the other way around as well. If people start selling their Kenshi tokens, then
there will be more Kenshi tokens in the pool and less BUSDs, making the price of Kenshi
tokens go lower. That's how the market works, it's a balance between supply and demand.

.. note::
  In the examples above, we used smaller numbers on purpose to make the calculations
  more readable. Actuall numbers deployed to the Kenshi / BUSD pool are much bigger
  than the ones used above.

.. _PancakeSwap: https://pancakeswap.finance

Improving the Price
-------------------

There are several ways to improve the price of Kenshi tokens, one obvious method is to
buy and hold, and invite others to do so. By sharing Kenshi projects on social media and
inviting others to the project you can improve the price of Kenshi tokens. Futhermore, this
will bring more profits to the system, making us able to buy back more Kenshi tokens to
be distributed to the holders.

Another way of improving the price is through burning. When a burning process happens
a certain amount of Kenshi tokens are taken out of circulation, which means they will never
get added to the pool ever again. Doing this guarantees there will be more and more BUSDs 
against Kenshi tokens in the pool as we move forwards, making the price of Kenshi tokens
go higher over time.