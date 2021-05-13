from flask import Flask, request
import re
import os
import argparse
import sys

app = Flask(__name__)

def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Start HTTP Server')

    parser.add_argument(
        '-P', '--port',
        help='port to start HTTP server on',
        type=int)
    return parser.parse_args(args)

def camel_case_split(str):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

@app.route("/helloworld")
def stranger():
    if request.args.get('name') == None:
        return("Hello Stranger")
    else:
        stringToSplit = request.args.get('name')
        splitString = camel_case_split(stringToSplit)
        value = ' '.join(splitString)
        return(value)

@app.route("/versionz")
def versionz():
    hash = os.environ.get('HASH')
    app_name = os.environ.get('APP_NAME')
    response = {
        "hash" : hash,
        "app_name" : app_name
    }
    return response

if __name__ == "__main__":
    color = os.getenv('COLOR','RED')
    print(color)
    opts = parse_args(sys.argv[1:])
    port = opts.port
    if port == None:
        port = 8080
    app.run(host='0.0.0.0',port=port)
