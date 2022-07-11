Example
=======

The following Solidity code implements a D20 smart contract using
the Kenshi VRF service.

This contract is deployed to and is testable on all Kenshi supported blockchains,
you can find the contract address on the next section.

.. admonition:: What is a D20?
  :class: hint

  The D20 is a 20-sided die. The d20 System is a role-playing game system published in 2000 by
  Wizards of the Coast, originally developed for the third edition of Dungeons & Dragons.
  The system is named after the 20-sided dice which are central to the core mechanics of many
  actions in the game. [#f1]_

.. seealso::

    This example is also available on `GitHub <https://github.com/KenshiTech/d20>`_.

D20 Smart Contract
------------------

.. code-block:: solidity

  //SPDX-License-Identifier: Apache-2.0
  pragma solidity ^0.8.11;

  import "@kenshi.io/vrf-consumer/contracts/VRFConsumer.sol";

  contract D20 is VRFConsumer {
      mapping(uint256 => address) requests;
      address _owner;

      constructor() {
          _owner = msg.sender;
      }

      /**
      * @dev this function can be used to pass config parameters
      * to the Kenshi VRF library
      */
      function setVRFConfig(address coordinator) public {
          require(msg.sender == _owner, "Only owner");
          setupVRF(coordinator);
      }

      /**
      * @dev rolls a D20, requests a random number from the Kenshi VRF coordinator
      * and maps the `requestId` of the VRF request to the message sender
      */
      function roll() public {
          uint256 requestId = requestRandomness();
          requests[requestId] = msg.sender;
      }

      event Rolled(address addr, uint8 number);

      /**
      * @dev receives `requestId` and `randomness` from the Kenshi VRF coordinator,
      * gets the original message sender, converts the randomness to a number between
      * 1 and 20, and emits an event as the D20 roll result for this `requestId`
      */
      function fulfillRandomness(uint256 requestId, uint256 randomness)
          internal
          override
      {
          address addr = requests[requestId];
          uint8 number = uint8(1 + (randomness % 20));
          emit Rolled(addr, number);
      }
  }

After deploying the above example, you need to call the ``setVRFConfig`` function with
appropriate parameters depending on the chain your contract is deployed to. This
information can be found in the next section.

.. hint::
    
    Exposing a public function for setting the VRF config is not required, you can just
    call the ``setupVRF`` function inside your contract constructor. However, we highly
    recommend exposing such a functionality to make your VRF version upgradable.

.. [#f1] https://en.wikipedia.org/wiki/D20_System