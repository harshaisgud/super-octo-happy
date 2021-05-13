# CamelCaseSplit
A Sample HTTP server that splits camel case words supplied to it using query parameters.
Repository also includes ways to deploy to a local Kubernetes cluster.

## Endpoint Details
This http server includes two endpoints :

- /helloworld
    This endpoint accepts query parameter of name. If no query parameter or one other than name is provided the endpoint returns the text `Hello Stranger`.
    When a the name query parameter is provided , the text is split accoring to camel case.
    For example `IP:PORT/helloword?name=HarshaSri` returns `Harsha Sri`.
- /versionz
    This endpoint returns the name of the application and the hash of the current commit of the code.

## Usage Details

### Running it locally using make
Run and test the application with the command `make setup && make test && make run_default`.
This starts the server by on port 8080 by default.

To run the app on a custom port export a shell variable using `export PORT=5000` and modify the above command to
`make setup && make test && make run`.

### Running it locally using python3
The application can be started on a custom port with `python3 app.py [--port|-P]`. The default port is `8080`.