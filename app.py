from flask import Flask, request
import re
import os
import argparse
import sys
from logging.config import dictConfig
import requests
import json

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    func() 
 
def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Start HTTP Server')

    parser.add_argument(
        '-P', '--port',
        help='port to start HTTP server on',
        type=int)
    return parser.parse_args(args)

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

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
    versionz_endpoint = os.getenv('VERSIONZ_EP')
    if versionz_endpoint == None:
        hash = os.environ.get('HASH')
        app_name = os.environ.get('APP_NAME')
        response = {
            "hash" : hash,
            "app_name" : app_name
        }
        return response
    else:
        if "http://" not in versionz_endpoint:
            versionz_endpoint = "http://" + versionz_endpoint
        versionz_response = requests.get(versionz_endpoint)
        response = json.loads(versionz_response.content.decode('utf-8'))
        response['resp_time'] = str(versionz_response.elapsed.total_seconds()) + 's'
        return response
        
        

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    color = os.getenv('COLOR')
    print(color)
    opts = parse_args(sys.argv[1:])
    port = opts.port
    if port == None:
        port = 8080
    app.run(host='0.0.0.0',port=port)
