Example
=======

Below is an example Sync task definition:

.. code-block:: json

  {
    "interval": "5 seconds",
    "blockchain": "binance-mainnet",
    "fromBlock": 13623924,
    "step": 12,
    "signature": "Transfer(address,address,uint256)",
    "abi": ["event Transfer(address indexed from, address indexed to, uint256 value)"],
    "args": [null, "0x000000000000000000000000B61E6153b909CB7e1696F76b703dAceb3B8AD3b5"]
  }
