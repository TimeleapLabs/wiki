Examples
========

On this page you can find examples for `Node.js`_, Python_ and Go_ languages.

Node.js
-------

.. tabbed:: axios

  .. note:: This example requires Node.js v14.8+ and the axios npm package installed.

  .. code-block:: javascript

    import axios from "axios";

    /**
    * This is the Kenshi Deep Index endpoint for GraphQL
    */
    const endpoint = "https://api.kenshi.io/index/graphql";

    /**
    * Define your GraphQL query here
    */
    const query = `{
        getEntries(blockchain: "binance-testnet") {
          event {
            name
          }
        }
      }`;

    /**
    * POST request sending the GraphQL query to the
    * Kenshi Deep Index endpoint, receive the data and print
    */
    const { data } = await axios.post(endpoint, { query });
    console.log(data);


.. tabbed:: node-fetch

  .. note:: This example requires Node.js v14.8+ and the node-fetch npm package installed.

  .. code-block:: javascript

    import fetch from "node-fetch";

    /**
    * This is the Kenshi Deep Index endpoint for GraphQL
    */
    const endpoint = "https://api.kenshi.io/index/graphql";

    /**
    * Define your GraphQL query here
    */
    const query = `{
      getEntries(blockchain: "binance-testnet") {
        event {
          name
        }
      }
    }`;

    /**
    * POST request sending the GraphQL query to the
    * Kenshi Deep Index endpoint
    */
    const response = await fetch(endpoint, {
      method: "POST",
      body: JSON.stringify({ query }),
    });

    /**
    * Receive the data and print it
    */
    const { data } = await response.json();
    console.log(data);

Python
------

.. tabbed:: requests

  .. note:: This example requires the requests Python package installed.

  .. code-block:: python

    import requests

    # This is the Kenshi Deep Index endpoint for GraphQL
    endpoint = "https://api.kenshi.io/index/graphql"

    # Define your GraphQL query here
    query = """{
        getEntries(blockchain: "binance-testnet") {
            event {
                name
            }
        }
    }"""

    # POST request sending the GraphQL query to the
    # Kenshi Deep Index endpoint
    response = requests.post(endpoint, json={"query": query})

    # Receive the data and print it
    data = response.json()["data"]
    print(data)

Go
--

.. tabbed:: shurcool/graphql

  .. note:: This example requires the shurcool/graphql package installed.

  .. code-block:: go

    package main

    import (
      "context"
      "fmt"

      "github.com/shurcool/graphql"
    )

    func main() {
      /**
      * This is the Kenshi Deep Index endpoint for GraphQL
      */
      endpoint := "https://api.kenshi.io/index/graphql"

      /**
      * Create a GraphQL client to connect to the GraphQL endpoint
      */

      client := graphql.NewClient(endpoint, nil)

      /**
      * Define your GraphQL query here
      */
      var query struct {
        GetEntries []struct {
          Event struct {
            Name graphql.String
          }
        } `graphql:"getEntries(blockchain: \"binance-testnet\")"`
      }

      /**
      * Send the query to the GraphQL server
      */
      err := client.Query(context.Background(), &query, nil)

      /**
      * Check for errors and print the retrieved data
      */
      if err != nil {
        fmt.Println(err)
      } else {
        fmt.Println(query.GetEntries)
      }
    }
