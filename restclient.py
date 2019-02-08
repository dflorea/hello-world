# The is the REST API server side code
# Jacob Jensen - copyright 2019
# DANJACOB project
# pip install flask flask_restful Flask-Jsonpify
# pip install Flask-MySQL

# http://35.175.141.30:5002/pictures

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

import requests

resp = requests.get('http://52.207.248.24:5002/picture')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /picture/ {}'.format(resp.status_code))
for respitem in resp.json():
    print(respitem)
