API Interface
=============

VRF Consumer
------------

To request a verifiable random number, your smart contract should inherit from this
library. To see an example of doing that refer to our `D20 example`_. The VRF Consumer
provides the following functions:

.. _`D20 example`: https://github.com/KenshiTech/d20

- **setupVRF**: This function is overloaded and accepts either one or three arguments:
  The VRF coordinator address, a boolean value indicating if the received VRF results
  should be verified on the chain, and a boolean value indicating if ``randomnessFulfilled``
  events should be emitted. The two latter arguments are optional and default to ``false``.
  Notes: This function automatically retrieves the VRF Utils address from the VRF coordinator
  and sets it up for you.

- **setVRFCoordinatorAddr**: Used to set the VRF coordinator address for requesting randomness.
  This function does NOT automatically setup VRF Utils.

- **setVRFUtilsAddr**: Used to set the VRF Utils address. The VRF Utils contract is used to verify
  randomness on the chain. This library is also used to derive the beta value and generate a random
  number from the VRF proof.

- **setVRFShouldVerify**: Sets if the randomness should be verified on the chain. This will increas
  the gas used significantly.

- **setVRFIsSilent**: Sets if the ``randomnessFulfilled`` should be emitted. Turn off for gas saving.

- **requestRandomness**: Calls the ``requestRandomness`` method of the VRF coordinator. You should call
  this method each time you need a random number. Returns the ``requestId``, you can store this value
  to map VRF results with a user request.

- **onRandomnessReady**: This function is called by the VRF coordinator when the VRF results are ready.

- **fulfillRandomness**: An abstract function that does nothing. This is called by the ``onRandomnessReady``
  function when a VRF result is received and verified. You need to re-implement this in your smart contract.
  Anything you need to do with the randomness you requested should be implemented here.

For function signatures check the `VRF consumer repositorty`_.

.. _`VRF consumer repositorty`: https://github.com/KenshiTech/vrf-consumer

VRF Utils
---------

The VRF Utils Solidity library is released in source form together with a JavaScript VRF implementation
library. This library is deployed to all chains and is made available free of charge to anyone who finds
a use for it. This library is used by the Kenshi consumer for calculating the VRF beta which is used to
generate randomness on chain. It is also used to verify the VRF results on chain.

Refer to the `VRFUtils.sol file`_ on Github to check the available functions. Read the `ECVRF draft`_ to
learn more about each function.

.. _`VRFUtils.sol file`: https://github.com/KenshiTech/vrf-consumer/blob/master/contracts/VRFUtils.sol
.. _`ECVRF draft`: https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-vrf-10.html
