.. role:: datatype(code)
   :language: javascript

Schema
======

Below you can find the Kenshi Reverse-API request body schema.

.. list-table::
   :header-rows: 1
   :widths: 20 8 50

   * - Field
     - Type
     - Description
   * - ``entry``
     - :datatype:`Object`
     - The parsed log entry received from the blockchain
   * - ``entry._id``
     - :datatype:`String`
     - String ID of this record in the Kenshi database cluster
   * - ``entry.log``
     - :datatype:`Object`
     - Information about the event log
   * - ``entry.log.index``
     - :datatype:`String`
     - Hex representation of the log index
   * - ``entry.transaction``
     - :datatype:`Object`
     - Information about the transaction
   * - ``entry.transaction.index``
     - :datatype:`String`
     - Hex representation of the transaction index
   * - ``entry.transaction.hash``
     - :datatype:`String`
     - Hex representation of the transaction hash
   * - ``entry.block``
     - :datatype:`Object`
     - Information about the block
   * - ``entry.block.address``
     - :datatype:`String`
     - Hex representation of the contract address emitting the event
   * - ``entry.block.hash``
     - :datatype:`String`
     - Hex representation of the block hash
   * - ``entry.block.number``
     - :datatype:`Number`
     - The block number
   * - ``entry.event``
     - :datatype:`Object`
     - Information about the emitted event
   * - ``entry.event.name``
     - :datatype:`String`
     - Name of the emitted event
   * - ``entry.event.signature``
     - :datatype:`String`
     - Signature of the emitted event
   * - ``entry.event.args``
     - :datatype:`Object`
     - Parsed arguments for the emitted event
   * - ``entry.event.args.$``
     - :datatype:`String`
     - Hex value of an argument where $ is the argument name
   * - ``entry.createdAt``
     - :datatype:`String`
     - ISO string of the date when this record was created in the Kenshi database cluster
   * - ``taskId``
     - :datatype:`String`
     - The ``taskId`` associated with your event listener task
   * - ``blockchain``
     - :datatype:`String`
     - Name of the chain, possible values are:

       ``binance-mainnet``, ``binance-testnet``, ``polygon-mainnet``, ``polygon-mumbai``,
       ``fantom-mainnet``, ``fantom-testnet`` [#f1]_

.. [#f1] Currently only the testnet networks are available.
