from flask import Flask, request
from flask_restful import Resource, Api
from routes.graphPosition import graphPosition

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return "Hello World"


api.add_resource(graphPosition, '/graph')

if __name__ == '__main__':
    app.run(debug=True)
