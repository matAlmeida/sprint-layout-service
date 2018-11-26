import os
from flask import Flask
from flask_restful import Api
from routes.graphPosition import graphPosition

app = Flask(__name__)
api = Api(app)


@app.route('/')
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
        app.run(port=port)
