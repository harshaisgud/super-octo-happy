# CamelCaseSplit
A Sample HTTP server that splits camel case words supplied to it using query parameters.
Repository also includes ways to deploy to a local Kubernetes cluster.

## Endpoint Details
This http server includes two endpoints :

- /helloworld
    This endpoint accepts query parameter of name. If no query parameter or one other than name is provided the endpoint returns the text `Hello Stranger`.
    When the name query parameter is provided , the text is split accoring to camel case.
    For example `IP:PORT/helloworld?name=HarshaSri` returns `Harsha Sri`.
- /versionz
    This endpoint returns the name of the application and the githash of the current commit of the code.

## Usage Details

### Running it locally using make
Run and test the application with the command `make setup && make test && make run_default`.
This starts the server by on port 8080 by default.

To run the app on a custom port export a shell variable using `export PORT=5000` and modify the above command to
`make setup && make test && make run`.

### Running it locally using python3
The application can be started on a custom port with `python3 app.py [--port|-P]`. The default port is `8080`.

### Running it locally using docker
The docker file has been included to build the image. Build Image with `docker build -f Dockerfile . --build-arg GITHASH=value`
where `GITHASH` is the value of githash of current commit. It can be obtained by running `git rev-parse HEAD`

### Deploy to kubernetes 
The application has been packaged as a chart and can be installed using the command `helm install release-name terraform/camelchart`


## Jenkins Docker File
A modified dockerfile for creating jenkins with the required binaries i.e kubectl and terraform has been added .