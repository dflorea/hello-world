# The is the REST API server side code
# Jacob Jensen - copyright 2019
# DANJACOB project
# pip install flask flask_restful
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
#from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class Picture(Resource):
    def get(self):
        return {'nothing yet'}
        #return jsonify(result)

api.add_resource(Picture, '/picture') # Route_1

if __name__ == '__main__':
	#app.run(port='5002')
	app.run(port='5002', host='52.207.248.24')
