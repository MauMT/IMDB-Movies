from flask import Flask, request
from movies import models, movieOutput
import json

app = Flask(__name__)
models.start_mappers()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route("/moviesByMagicKey/<magicKey>/sorted=<sorted>", methods=["GET"])
def get_movies(magicKey, sorted):
    return json.dumps(movieOutput.getMovieByMagicKey(magicKey)), 200