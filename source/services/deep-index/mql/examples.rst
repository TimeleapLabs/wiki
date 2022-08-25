Examples
========

On this page, you can find examples for `Node.js`_, Python_ and Go_ languages.

Node.js
-------

.. tabbed:: axios

  .. note:: This example requires Node.js v14.8+ and the axios npm package installed.

  .. seealso::
    This example is also available on `GitHub <https://github.com/KenshiTech/mql-example-node-axios>`__

  .. code-block:: javascript

    import axios from "axios";

    /**
    * This is the Kenshi Deep Index endpoint for MQL
    */
    const endpoint = "https://api.kenshi.io/index/mql";
    const apikey = "YOUR_API_KEY";
    const owner = "YOUR_WALLET_ADDRESS";

    /**
    * Define your MQL request here
    */
    const request = {
      blockchain: "binance-mainnet",
      owner,
      apikey,
      query: {
        "event.name": "Transfer",
        "block.number": { $gte: 20740000 },
      },
    };

    /**
    * Post request sending the MQL request to the
    * Kenshi Deep Index endpoint, receive the data and print
    */
    const data = await axios.post(endpoint, request);
    console.log(data);



.. tabbed:: node-fetch

  .. note:: This example requires Node.js v14.8+ and the node-fetch npm package installed.

  .. seealso::
    This example is also available on `GitHub <https://github.com/KenshiTech/mql-example-node-fetch>`__

  .. code-block:: javascript

    import fetch from "node-fetch";

    /**
    * This is the Kenshi Deep Index endpoint for MQL
    */
    const endpoint = "https://api.kenshi.io/index/mql";
    const apikey = "YOUR_API_KEY";
    const owner = "YOUR_WALLET_ADDRESS";

    /**
    * Define your MQL request here
    */
    const request = {
      blockchain: "binance-mainnet",
      owner,
      apikey,
      query: {
        "event.name": "Transfer",
        "block.number": { $gte: 20740000 },
      },
    };

    /**
    * Post request sending the MQL request to the
    * Kenshi Deep Index endpoint
    */
    const response = await fetch(endpoint, {
      method: "POST",
      body: JSON.stringify(request),
    });

    /**
    * Receive the data and print it
    */
    const data = await response.json();
    console.log(data);


Python
------

.. tabbed:: requests

  .. note:: This example requires the requests Python package installed.

  .. seealso::
    This example is also available on `GitHub <https://github.com/KenshiTech/mql-example-python>`__

  .. code-block:: python

    import requests

    # This is the Kenshi Deep Index endpoint for MQL
    endpoint = "https://api.kenshi.io/index/mql"

    # Define your MQL query here
    request = {
        "blockchain": "binance-mainnet",
        "owner": "YOUR_WALLET_ADDRESS",
        "apikey": "YOUR_API_KEY",
        "query": {
            "event.name": "Transfer",
            "block.number": {"$gte": 20740000},
        },
    }

    # Post request sending the MQL request to the
    # Kenshi Deep Index endpoint
    response = requests.post(endpoint, json=request)

    # Receive the data and print it
    data = response.json()
    print(data)

Go
--

.. tabbed:: net/http

  .. seealso::
    This example is also available on `GitHub <https://github.com/KenshiTech/mql-example-go>`__

  .. code-block:: go

    package main

    import (
      "bytes"
      "fmt"
      "io/ioutil"
      "net/http"
    )

    func main() {
      /**
      * This is the Kenshi Deep Index endpoint for MQL
      */
      endpoint := "https://api.kenshi.io/index/mql"

      /**
      * Define your MQL request here
      */
      var mql = []byte(`{
        "blockchain": "binance-mainnet",
        "owner": "YOUR_WALLET_ADDRESS",
        "apikey": "YOUR_API_KEY",
        "query": {
          "event.name": "Transfer",
          "block.number": {
            "$gte": 20740000
          }
        }
      }`)

      /**
      * Post request sending the MQL request to the
      * Kenshi Deep Index endpoint, receive the data and print
      */
      req, err := http.NewRequest("POST", endpoint, bytes.NewBuffer(mql))
      req.Header.Set("Content-Type", "application/json; charset=UTF-8")

      client := &http.Client{}
      resp, err := client.Do(req)

      if err != nil {
        panic(err)
      }

      defer resp.Body.Close()
      body, _ := ioutil.ReadAll(resp.Body)
      fmt.Println(string(body))
    }

