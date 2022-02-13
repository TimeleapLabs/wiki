Example
=======

Below is an example listener task definition:

.. code-block:: json

  {
    "interval": "5 seconds",
    "syncTaskId": "61ffd674729bf8e4453ebefd",
    "query": {
      "block.address": "0xd2e91f803e052167bf2364e9566f30eb695988fe",
      "event.name": "RandomnessRequested"
    },
    "fromBlock": 16518963,
    "step": 12,
    "blockchain": "binance-testnet",
    "context": { "url": "https://rapi.kenshi.io" }
  }
