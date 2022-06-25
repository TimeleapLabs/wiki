Example
=======

The example below shows a Sync task to sync all Kenshi token transfer events into the Kenshi
blockchain data clusters:

.. role:: data(code)
   :language: javascript

.. list-table::
   :header-rows: 1
   :widths: 20 8 50

   * - Field
     - Value
     - Description
   * - Chain
     - BNB Chain
     - Kenshi smart contract is deployed to the BNB Chain.
   * - Starting block
     - 17633890
     - Kenshi smart contract is deployed at block number 17633890.
   * - Interval
     - 5 seconds
     - The faster, the better
   * - Step
     - 12 blocks
     - Making sure no events escape
   * - Timeout
     - 10 seconds
     - 10 seconds timeout for 12 blocks at a time seems reasonable.
   * - Duration
     - N/A
     - Not applicable
   * - Contract address
     - :data:`0x42f9c5a27a2647a64f7D3d58d8f896C60a727b0f`
     - This is the Kenshi token smart contract address
   * - Contract ABI
     - :data:`[ "event Transfer(address indexed from, address indexed to, uint256 value)" ]`
     - Human-Readable ABI including only the ``Transfer`` event ABI
   * - Event signature
     - :data:`Transfer(address,address,uint256)`
     - Event signature for the Transfer event
   * - Arguments
     - 
     - Left empty to sync all Transfer events
