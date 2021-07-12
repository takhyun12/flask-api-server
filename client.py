__version__ = '1.0.0'

import requests

url = 'http://127.0.0.1:8080/serial'
response = requests.get(url)
serial_dict = response.json()
print(serial_dict)
