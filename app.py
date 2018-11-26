import os
from flask import Flask, request
from flask_restful import Resource, Api
from routes.graphPosition import graphPosition

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    request_format = [
        {"label": 1, "links": [2, 3]},
        {"label": 2, "links": [1, 3]},
        {"label": 3, "links": [1, 2]}
    ]
    response_format = [
        {
            "label": 1,
            "pos": [6, 0],
            "links": [2, 3]
        },
        {
            "label": 2,
            "pos": [9, 8],
            "links": [3]
        },
        {
            "label": 3,
            "pos": [1, 7],
            "links": []
        }
    ]
    return {
        "message": "Make a POST to this URL with the following format and passing the max size eg: url/graph?size=9",
        "request-format": request_format,
        "response-format": response_format
    }


api.add_resource(graphPosition, '/graph')

if __name__ == '__main__':
    port = os.environ['PORT']
    if port == None:
        app.run(debug=True)
    else:
        app.run(port=port)
