from flask import Flask, request
import re
import os

app = Flask(__name__)


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
    print(hash)
    response = {
        "hash" : hash,
        "app_name" : app_name
    }
    return response

if __name__ == "__main__":
    color = os.getenv('COLOR','RED')
    print(color)
    app.run()

def camel_case_split(str):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)