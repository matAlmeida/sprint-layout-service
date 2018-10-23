from flask import request
from flask_restful import Resource
import networkx as nx
import math as mt


class graphPosition(Resource):
    def get(self):
        request_format = [
            {"label": 1, "links": [2, 3]},
            {"label": 2, "links": [1, 3]},
            {"label": 3, "links": [1, 2]}
        ]
        response_format = [
            {
                "label": "1",
                "pos": {
                    "x": 6,
                    "y": 0
                }
            },
            {
                "label": "2",
                "pos": {
                    "x": 9,
                    "y": 8
                }
            },
            {
                "label": "3",
                "pos": {
                    "x": 1,
                    "y": 7
                }
            }
        ]
        return {
            "message": "Make a POST to this URL with the following format",
            "request-format": request_format,
            "response-format": response_format
        }

    def post(self):
        G = nx.Graph()
        jsonNodes = request.get_json()
        nodes = []
        edges = []
        for node in jsonNodes:
            # print(node)
            label = node['label']
            links = node['links']
            nodes.append(label)
            for link in links:
                if (link > label):
                    edges.append((label, link))

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        pos = nx.spring_layout(G, scale=4.5)

        retArray = []

        for i in pos:
            x = mt.ceil(float(pos[i][0]) + 4.5)
            y = mt.ceil(float(pos[i][1]) + 4.5)

            node = {}
            node['label'] = str(i)
            node['pos'] = {"x": x, "y": y}
            retArray.append(node)

        return {"message": retArray}
