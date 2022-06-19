from flask import Flask, request
from movies import models, movieOutput
import json

app = Flask(__name__)
models.start_mappers()


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200


@app.route('/moviesByMagicKey/<magicKey>/', defaults={'rating': "True"})
@app.route('/moviesByMagicKey/<magicKey>/rating=<rating>')
def show(magicKey, rating):
    if (int(magicKey) >  4 or int(magicKey) < 1 ):
        return "Magic Key must be between 1 and 4", 400
    else:
        return json.dumps(movieOutput.getMovieByMagicKey(magicKey, rating)), 200
    pass