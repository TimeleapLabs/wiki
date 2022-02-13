.. role:: datatype(code)
   :language: javascript

Schema
======

Below you can find the Kenshi Sync task definition schema.

.. list-table::
   :header-rows: 1
   :widths: 10 16 50

   * - Field
     - Type
     - Description
   * - interval
     - :datatype:`String`
     - Interval of running the Sync task
   * - signature
     - :datatype:`String`
     - Event signature [#f1]_
   * - name
     - :datatype:`String`
     - Event name [#f1]_
   * - abi
     - :datatype:`[String]`
     - Human readable ABI array for parsing the event
   * - args
     - :datatype:`[String || null]`
     - Arguments array for constructing an event filter
   * - fromBlock
     - :datatype:`Number`
     - Starting block of the Sync task
   * - step
     - :datatype:`Number`
     - How many steps to sync per run
   * - blockchain
     - :datatype:`String`
     - Name of the chain, available values are:

       binance-mainnet, binance-testnet, polygon-mainnet, polygon-mumbai,
       fantom-mainnet, fantom-testnet

.. [#f1] One of ``signature`` or ``name`` is required.