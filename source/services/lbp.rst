Liquidity Bootstrapping
=======================

The Kenshi Liquidity Bootstrapping Oracle helps kickstart token projects
with a low liquidity at a fair launch price. This is the right tool if you
want a controlled pricing for your token, or you don't want to offer your 
token at a very low price because you lack the needed capital.

This oracle is also usable if you have a percentage of your tokens locked
away, and you want to inject them into your liquidity pool at certain times
or on certain events. This page has some useful information about the functionality
of this oracle, you can also contact us if you have any unanswered questions.

What's a Liquidity Bootstrapping Pool?
--------------------------------------

In a traditional liquidity pool, there are a pair of tokens with a ratio of 1:1
and the pricing is defined based on the following formula:

.. math::
  X \times Y = Constant

Where X and Y are the two tokens making up the pair. This formula works very
well when a project has a decent size of capital to pair with their own newly
made tokens. However, when a project lacks liquidity this formula results in
a low initial token price, and possibly huge buys and whales at the start.

As an example, if you pair 100% of the tokens your project creates with $1000
worth of USDT, then anyone will be able to buy half of your entire supply for $500,
which isn't that much. So, what's the solution to that? One obvious solution is to
put more capital into your liquidity pool, for example to pair your tokens with
$100k instead of $1k.

Another solution is to offer only a percentage of your tokens for the low capital
you've got. However, if you go this way, you'll have to pair the rest of your tokens
with a lot more than what you initially did at launch, because the token price keeps
going up while you're busy working out the capital for the rest of your supply.

Both proposed solutions require a lot of capital, either at the start or in the
long run. What Kenshi offers is a mix of the two, plus a small tax on each purchase
transaction your clients make. With Kenshi, you will offer a percentage of your tokens
against the capital you have, then you will use the tax you gather from the transactions
to inject the rest of the tokens into your liquidity pool.

How does it work?
-----------------

Instead of offering 100% of your total supply, you will pair a small percentage of them
with the token of your choice, and lock away the rest either in the smart contract or in
a special address.

The Kenshi Liquidity Bootstrapping Bot listens to all ``Transfer`` events on your
smart contract, detecting when someone is making a purchase from your liquidity
pool. The bot then checks the amount of tokens transfered from the pool to the outside,
and restores it by taking the same amount of tokens from your locked tokens balance.

Half of the tokens taken out of the locked balance are then sold to the liquidity pool
to get an equivalent amount of the pairing token. This amount of pairing tokens are then
paired with the remaining half of the tokens taken out of the locked balance and are put
back into the pool, effectively keeping the amount of your tokens in the pool a constant.

This process continues until all of your locked tokens are injected into the pool. This
way you're offering your tokens at a higher initial price and liquidity builds up in
your pool as we move on. You can consider this an indirect purchase tax paid by your
customers when they buy your tokens.

This indirect tax is very small and so is the price impact of the trades made by the bot.
The tax and the price impact get smaller and smaller as more tokens are injected into the
liquidity pool, until there is no more tokens left in the locked balance, in which case
the pool returns back to a standard AMM formula.