import os

import requests

URL = "http://127.0.0.1:5000/upload"

config_file = "testfile.conf"
with open(os.path.join(config_file), "rb") as file:
    file_read = file.read()

json_data = {config_file: file_read.decode(),
             "password": "c3VwCg=="}
headers = {"content-type": "application/json",
           "pass": "secret"}
requests.post(url=URL, headers=headers, json=json_data)
