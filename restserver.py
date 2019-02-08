# The is the REST API server side code
# Jacob Jensen - copyright 2019
# DANJACOB project
# pip install flask flask_restful
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask import jsonify

app = Flask(__name__)
api = Api(app)

class Picture(Resource):
    def get(self):
        return jsonify('waiting for the AI picture code to complete')

api.add_resource(Picture, '/picture') # Route_1

if __name__ == '__main__':
	#app.run(port='5002')
	app.run(port='5002', host='0.0.0.0')
