.. role:: datatype(code)
   :language: javascript

Schema
======

Below you can find the Kenshi event listener task definition schema.

.. list-table::
   :header-rows: 1
   :widths: 10 5 50

   * - Field
     - Type
     - Description
   * - ``interval``
     - :datatype:`String`
     - Interval of running the listener task
   * - ``syncTaskId``
     - :datatype:`String`
     - The ``taskId`` of the Sync task associated with this listener task
   * - ``context``
     - :datatype:`Object`
     - Context object holding info about the R-API endpoint
   * - ``context.url``
     - :datatype:`String`
     - URL of the R-API endpoint
   * - ``query``
     - :datatype:`Object`
     - A valid MongoDB query object
   * - ``fromBlock``
     - :datatype:`Number`
     - Starting block of the event listener task
   * - ``step``
     - :datatype:`Number`
     - How many steps to sync per run
   * - ``blockchain``
     - :datatype:`String`
     - Name of the chain, available values are:

       binance-mainnet, binance-testnet, polygon-mainnet, polygon-mumbai,
       fantom-mainnet, fantom-testnet [#f1]_

.. [#f1] Currently only the testnet networks are available.

