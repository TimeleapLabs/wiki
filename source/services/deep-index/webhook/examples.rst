Examples
========

On this page you can find examples for `Node.js`_ and Python_.

Node.js
-------

.. tabbed:: express

  .. note:: This example requires the express npm package installed.

  .. seealso::
    This example is also available on `GitHub <https://github.com/kenshi-token/reverse-api-example-node>`__.

  .. code-block:: javascript

    import express from "express";
    import parser from "body-parser";

    /**
    * Creat an express app
    */
    const app = express();
    app.use(parser.json());

    /**
    * Create a POST endpoint for receiving data from
    * the Kenshi Event Dispatcher
    */
    app.post("/", (req, res) => {
      /**
      * Details for the received blockchain event are
      * in the request body
      */
      console.log(req.body);
      /**
      * Your endpoint must return a status code bigger
      * than or equal to 200, and lower than 300. Any
      * other code is considered an error and results
      * in a retry.
      */
      res.status(200).end("OK");
    });

    /**
    * Listen on port 8080
    * Note: You don't necessarily need to listen on this
    * port, this is just an example
    */
    app.listen(8080, () => console.log(`Started server at http://localhost:8080!`));


Python
------

.. tabbed:: flask

  .. note:: This example requires the flask Python package installed.

  .. seealso::
    This example is also available on `GitHub <https://github.com/kenshi-token/reverse-api-example-python>`__.

  .. code-block:: python

    from flask import Flask, request

    # Create a flask app
    app = Flask(__name__)

    # Setup a POST endpoint for receiving data from
    # the Kenshi Event Dispatcher
    @app.route("/", methods=["POST"])
    def add_message():
        # Details for the received blockchain event are
        # in the request body
        print(request.json)
        # Your endpoint must return a status code bigger
        # than or equal to 200, and lower than 300. Any
        # other code is considered an error and results
        # in a retry.
        return "OK", 200


    if __name__ == "__main__":
        # Listen on port 8080
        # Note: You don't necessarily need to listen on this
        # port, this is just an example
        app.run(host="0.0.0.0", port=8080)

