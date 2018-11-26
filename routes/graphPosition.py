import json
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
        ret = {
            "message": "Make a POST to this URL with the following format and passing the max size eg: url/graph?size=9",
            "request-format": request_format,
            "response-format": response_format
        }

        return json.dumps(ret, separators=(',', ':'))

    def post(self):
        G = nx.Graph()
        jsonNodes = request.get_json()
        max_size = float(request.args.get('size'))
        max_size /= 2
        nodes = []
        edges = []
        for node in jsonNodes:
            label = node['label']
            links = node['links']
            nodes.append(label)
            for link in links:
                if (link > label):
                    edges.append((label, link))

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)
        pos = nx.spring_layout(G, scale=max_size)

        retArray = []

        for i in pos:
            x = mt.ceil(float(pos[i][0]) + max_size)
            y = mt.ceil(float(pos[i][1]) + max_size)

            node = {}
            cleanLinks = [link for link in links if link > i]
            node['label'] = i
            node['pos'] = [x, y]
            node['links'] = cleanLinks
            retArray.append(node)

        ret = {"message": retArray}

        return json.dumps(ret, separators=(',', ':'))
