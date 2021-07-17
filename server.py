__version__ = '1.0.0'

from flask import Flask, request
from flask_restx import Api, Resource
import json


app = Flask(__name__)
api = Api(app, version='1.0.0')

json_data = open('./data/serial_data.json', encoding='UTF8')
serial_data: dict = json.load(json_data)


@api.route('/serial/<string:user_id>')
class Serial(Resource):
    @staticmethod
    def get(user_id):
        return [data for data in serial_data['data'] if data['user_id'] == user_id]


@api.route('/auth/sign_out/<string:user_id>')
class Auth(Resource):
    @staticmethod
    def post(user_id):
        return [data for data in serial_data['data'] if data['user_id'] == user_id]


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
