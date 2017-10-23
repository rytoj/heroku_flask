import os

import requests

URL = "https://save-config.herokuapp.com/"
URL = "http://127.0.0.1:5000/"

CONFIG_FILE = "db.json"


def post_data():
    """
    Post data to remote server
    :return: True if posted successfully, else return False
    """
    with open(os.path.join(CONFIG_FILE), "rb") as file:
        file_read = file.read()

    json_data = {CONFIG_FILE: file_read.decode(),
                 "password": "c3VwCg=="}
    headers = {"content-type": "application/json",
               "pass": "secret"}
    post = requests.post(url=URL, headers=headers, json=json_data)

    if post.status_code == 200:
        return True
    else:
        return False


def get_data():
    """

    :return: Returns file data from remote server
    """
    get_data = requests.get(URL + "get?file=db.json")
    get_data.status_code
    return get_data.content.decode()
