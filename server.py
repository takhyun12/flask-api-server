__version__ = '1.0.0'

from flask import Flask
from flask_restx import Api, Resource
import json


app = Flask(__name__)
api = Api(app)


@api.route('/serial')
class Api_Gateway(Resource):
    @staticmethod
    def get():
        try:
            with open('./data/serial_data.json', encoding='UTF8') as serial_json:
                serial_data: json = json.load(serial_json)
                return serial_data
        except FileNotFoundError:
            return None


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
