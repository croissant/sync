import os
import sys
import json
from flask import Flask
from flask import Response
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

sys.path.append("%s/lib" % os.path.dirname(os.path.abspath(__file__)))
import syncdb

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is first.'

@app.route('/list/<cid>')
def list(cid):
    return Response(json.dumps(syncdb.get_list(cid)), mimetype='application/json')

@app.route('/dic')
def dic():
    return Response(json.dumps({'this': 'is', 'dic': '.'}), mimetype='application/json')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
