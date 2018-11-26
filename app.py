import os
from flask import Flask
from flask_restful import Api
from routes.graphPosition import graphPosition

app = Flask(__name__)
api = Api(app)


@app.route('/', method=['GET'])
def index():
    return {
        "message": "Go to /graph"
    }


api.add_resource(graphPosition, '/graph')

if __name__ == '__main__':
    port = os.environ['PORT']
    if port is None:
        app.run(debug=True)
    else:
        print('running port {0}'.format(port))
        app.run(debug=True, use_reloader=True, port=port)
