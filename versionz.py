from flask import Flask, request
import re
import os
import argparse
import sys
from logging.config import dictConfig

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

@app.route("/")
def versionz():
    hash = os.environ.get('HASH')
    app_name = os.environ.get('APP_NAME')
    response = {
        "hash" : hash,
        "app_name" : app_name
    }
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
