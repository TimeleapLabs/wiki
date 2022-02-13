Getting Started
===============

The Kenshi VRF oracle implements a request-response message exchange pattern.
That means your smart contract needs to ask for a random number first, then
wait until our oracle answers to this random number request.

We implemented and provide a Solidity VRF consumer library you can use for
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

.. note::

  Make sure you have enough Kenshi tokens stored in your smart contract
  for paying the VRF fees. You can request testnet Kenshi by asking on our
  `Telegram chat`_.

.. _here: ./example.html
.. _`Telegram Chat`: https://t.me/kenshi_token

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

Kenshi implements the ERC1363_ payable token standard, exposing the ``verifyAndCall``
and ``transferAndCall`` functions. Your contract calls the ``verifyAndCall`` function
of our ERC1363 token, effectively calling the ``onApprovalReceived`` function on the
Kenshi VRF coordinator contract passing a ``requestId`` to it. If you inherit from
the Kenshi ``VRFConsumer`` library this is done automatically for you. To prevent
collisions, the library also increments the ``requestId`` for each request.

Once the call is received on the VRF coordinator, an event is emitted on the blockchain
that includes the address of your smart contract and the ``requestId`` of the request.
This event is then picked up by the Kenshi Deep Index Sync oracle, and passed to the
Kenshi VRF oracle using the Kenshi Deep Index Event Dispatcher.

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

.. _ERC1363: https://eips.ethereum.org/EIPS/eip-1363
