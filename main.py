"""
powerplant-coding-challenge
https://github.com/gem-spaas/powerplant-coding-challenge
"""

import json
import pprint
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from solve_functions import solve

app = Flask(__name__)
api = Api(app)

post_parser = reqparse.RequestParser()
post_parser.add_argument("request", type=str, help="main payload in str required", required=True)


class ProductionPlan(Resource):
    def post(self):
        args = post_parser.parse_args()

        r = json.loads(args["request"])
        pprint.pprint(r)

        res = solve(r)
        print("------------------------ BIG RESULT ------------------------")
        pprint.pprint(res)

        return res


api.add_resource(ProductionPlan, "/productionplan/")

if __name__ == "__main__":
    app.run(debug=True, port=8888)
