import json
from flask import Flask
from flask_restful import Api
from routes.graphPosition import graphPosition

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    ret = {
        "message": "Go to /graph"
    }

    return json.dumps(ret, separators=(',', ':'))


api.add_resource(graphPosition, '/graph')

if __name__ == '__main__':
    print('running')
    app.run(debug=True, use_reloader=True)
