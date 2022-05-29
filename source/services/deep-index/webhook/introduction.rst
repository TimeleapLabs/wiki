Introduction
============

Instead of querying the blockchain or the Kenshi GraphQL endpoint, you can get the
events delivered to your application instead. This allows creating a completely serverless
flow of receiving and processing the blockchain data.

The Kenshi Reverese-API service allows you to define a query, a starting block and an API
endpoint (your HTTP[S] endpoint, AWS Lambda function...), then every time your query matches
a record the Reverese-API service sends it to your endpoint.

To use this service head to the Kenshi dashboard_, connect your wallet and register an endpoint using
the new Reverese-API form. Continue reading on to get help with the dashboard or see examples of
the Reverese-API service.

.. _dashboard: https://kenshi.io/dashboard
