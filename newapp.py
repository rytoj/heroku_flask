import os

from flask import Flask, request

app = Flask(__name__)

SECRET_HEADER = "secret"
PASSWORD = "c3VwCg=="  # TODO: add from local env


@app.route("/")
def index():
    return "OK!"


@app.route("/user/<username>")
def show_profile(username):
    return "User %s " % username


def create_files(request_json):
    for file_name, data in request_json.items():
        with open(os.path.join("saved", file_name), "wb") as f:
            f.write(data.encode())


@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        password = request.environ.get("HTTP_PASS")
        if password == SECRET_HEADER:
            request_json = request.get_json()
            if request_json.get("password") == PASSWORD:
                request_json.pop("password")
                create_files(request_json)
                return "Posting", 200
        else:
            return "Wrong pass"
    if request.method == "GET":
        return "404", 404
    else:
        return "---"


if __name__ == "__main__":
    app.run()
