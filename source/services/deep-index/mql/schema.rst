Schema
======

Below you can find the Kenshi Deep Index MQL schemas.

Request
-------

.. list-table::
   :header-rows: 1
   :widths: 10 10 40

   * - Field Name
     - Type
     - Description
   * - ``blockchain``
     - ``String``
     - The blockchain you want to query.
   * - ``apikey``
     - ``String``
     - Your API key.
   * - ``owner``
     - ``String``
     - Wallet address the API key's owner.
   * - ``query``
     - ``Object``
     - Your MQL query. Refer to MongoDB documentation for more details.

Response
--------
  
.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Path
     - Type
   * - ``log.index``
     - ``String(Hex)``
   * - ``transaction.hash``
     - ``String(Hex)``
   * - ``transaction.index``
     - ``String(Hex)``
   * - ``block.number``
     - ``Number``
   * - ``block.hash``
     - ``String(Hex)``
   * - ``block.address``
     - ``String(Hex)``
   * - ``event.name``
     - ``String``
   * - ``event.signature``
     - ``String``
   * - ``event.args.${ARG_NAME}``
     - ``String(Hex)``
   * - ``createdAt``
     - ``String(ISODate)``

Available blockchains
---------------------

Available blockchains are:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Blockchain
     - MQL value
   * - BNB Chain
     - ``binance-mainnet``
   * - BNB Chain testnet
     - ``binance-testnet``
   * - Polygon
     - ``polygon-mainnet``
   * - Polygon Mumbai
     - ``polygon-mumbai``
   * - Fantom
     - ``fantom-mainnet``
   * - Fantom testnet
     - ``fantom-testnet``
   * - Avalanche
     - ``avalanche-mainnet``
   * - Avalanche Fuji
     - ``avalanche-fuji``
   * - Ethereum Goerli
     - ``ethereum-goerli``
