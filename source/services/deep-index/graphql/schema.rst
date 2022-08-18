Schema
======

Below you can find the Kenshi Deep Index GraphQL schema.

.. code-block:: graphql
  
  input ArgInput {
    name: String
    value: String
  }

  type Block {
    address: String
    number: Int
    hash: String
  }

  type Entry {
    _id: ID
    log: Log
    transaction: Transaction
    block: Block
    createdAt: AWSDateTime
    event: Event
  }

  type Event {
    name: String
    signature: String
    args: [[String]]
  }

  type Log {
    index: String
  }

  type Query {
    getEntries(
      blockchain: String!,
      args: [ArgInput],
      fromBlock: Int,
      toBlock: Int,
      address: String,
      event: String,
      signature: String,
      txHash: String,
      txIndex: String,
      logIndex: String,
      blockHash: String,
      owner: String,
      apikey: String
    ): [Entry]
  }

  type Transaction {
    hash: String
    index: String
  }

  schema {
    query: Query
  }

Available blockchains
---------------------

Available blockchains are:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Blockchain
     - GraphQL value
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
