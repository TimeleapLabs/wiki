Getting Started
===============

The Kenshi VRF oracle implements a request-response message exchange pattern.
That means your smart contract needs to ask for a random number first, then
wait until our oracle answers to this random number request.

We implement and provide a Solidity VRF consumer library you can use for
automatically handling the steps required for requesting and receiving a random
number. If you are interested in knowing how the process works you can read more
about the detailed steps in the `Kenshi VRF Workflow`_ section below.

.. tip::

  If you are using Hardhat or Truffle for development, you can install the Kenshi
  VRF consumer library using the following command:

  .. tabbed:: With NPM

    .. code-block:: bash

      npm install @kenshi.io/vrf-consumer

  .. tabbed:: With Yarn

    .. code-block:: bash

      yarn add @kenshi.io/vrf-consumer

VRF Subscriptions
-----------------

Kenshi dashboard_ can be to used create a VRF subscription. A subscription maps a Kenshi
payment to one or more contracts that use the Kenshi VRF. Every time one of these
contracts requests a VRF, the price for delivering the VRF to that contract is reduced
from the credit charged to the subscription.

This reduces gas fees and VRF delivery prices significantly, making it cheaper to
request randomness on the blockchain.

.. figure:: ../../_static/images/dashboard/vrf.png

  New VRF subscription form

.. _dashboard: https://kenshi.io/dashboard

To fill the form, you can refer to the following guide:

1. **Chain** is the chain you are targeting. This is the chain yoru smart contract is deployed to.
2. **Credit** is the amount of Kenshi you want to send to this subscription. This amount is consumed
   for paying the VRF fees requested by the **allow** list.
3. The **allow** list is a list of smart contract addresses you want to use this subscription for.
   These addresses must be checksummed.

Implementation
--------------

Kenshi implements the latest Goldberg ECVRF draft public by IETF. The latest version
of the original VRF document can be found on the IETF datatracker_.

Kenshi also publishes libraries for Node.js and Solidity that can be used for testing
the VRF functionality locally or other development purposes:

- `Node.js library`_
- `Solidity library`_ (located in ``contracts/lib`` directory and ``contracts/VRFUtils.sol``)

.. _datatracker: https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-vrf-10.html
.. _`Node.js library`: https://www.npmjs.com/package/@kenshi.io/node-ecvrf
.. _`Solidity library`: https://www.npmjs.com/package/@kenshi.io/vrf-consumer

Integration
-----------

To use the Kenshi VRF oracle for requesting random numbers, follow the steps below.

1. Install and import the Kenshi VRF consumer library
2. Inherit from the ``VRFConsumer`` smart contract
3. Call the ``setupVRF`` function with appropriate arguments
4. Implement a ``fulfillRandomness`` function
5. Call the ``requestRandomness`` function any time you need a new random number

An example of doing this can be found here_.

.. _here: ./example.html
.. _`Telegram Chat`: https://t.me/kenshi_developers

Using the randomness
--------------------

The ``randomness`` provided to your smart contract is an unsigned integer ranging
from ``0`` to ``2**256 - 1``. If you need a number ``K`` between a ``X`` and ``Y`` you
can use the following formula:

.. code-block:: solidity

  K = X + randomness % (Y - X)

``X`` being the smaller number. For example, to get a number between ``20`` and ``80``
you should use:

.. code-block:: solidity

  K = 20 + randomness % 60

Error-proof
-----------

The Kenshi VRF oracle tries reporting the random number back to your contract
a few times on different intervals before giving up. Failure to report a random
number can be caused by several factors such as network congestion or simply your
contract lacking enough Kenshi for paying the VRF fees.

Kenshi VRF Workflow
-------------------

Each time your smart contract calls the ``requestRandomness`` method of the Kenshi
VRF coordinator, it receives a ``requestId``. The Kenshi VRF coordinator keeps record
of the ``requestId`` for your smart contracts and increments it by one every time this
function is called from your smart contract.

An event is then emitted from the VRF coordinator that incldues this ``requestId``
as well as the address of your smart contract. This event is then picked up by the
Kenshi Deep Index Sync oracle, and passed to the Kenshi VRF oracle using the Kenshi
Deep Index Event Dispatcher.

Next the oracle combines the following parameters to create an alpha string that is
used for random number generation according to the Goldberg ECVRF draft 10 standard:

.. code-block:: javascript

  const alpha = sha256(transaction.hash + log.index + request.address + request.id)

Using the alpha constant and the draft 10 ``ECVRF-SECP256K1-SHA256-TAI`` cipher suite,
the Kenshi oracle generates the requested random number. After estimating the gas fee
needed for delivering it to your contract, it calls the ``fullfillRandomnessForContract``
function of the VRF coordinator.

This function then transfers enough Kenshi for paying the gas-fees as well as the VRF
generation fees from your contract address to our payment collector address. If the
transfer is successful the random number is delivered to your smart contract by calling the
``onRandomnessReady`` function inherited from the Kenshi ``VRFConsumer`` library in
your smart contract.

In case you set the ``verify`` parameter of the ``VRFConsumer`` to ``true``, the ``VRFConsumer``
verifies the received random number using the proof provided the Kenshi VRF oracle. This is
done by calling the ``VRFUtils`` contract deployed to the same chain as your smart contract.
The call reverts if the proof for the random number is invalid. When all the above steps are
executed successfully, the ``fulfillRandomness`` function is called on your smart contract,
passing the ``requestId`` and the ``randomness``.

