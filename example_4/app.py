# coding: utf-8

from flask import Flask, jsonify, request
from mongoengine import connect
import log_svc

app = Flask(__name__)
app.config.from_object('settings')
connect(host=app.config.get('DB_HOST'), port=app.config.get('DB_PORT'))


@app.route('/', methods=('GET', ))
def home():
    return jsonify(
        {
            'API': [
                '/closest_word',
                '/proximity'
            ]
        }
    )


@app.route('/closest_word', methods=('GET', ))
def closest_word():
    possibilities = request.args.get('possibilities').split(',')
    word = request.args.get('word')
    closest_word = log_svc.get_close_matches(word, possibilities)
    return jsonify({
        'closest_word': closest_word
    })


@app.route('/proximity', methods=('GET', ))
def proximity():
    word_a, word_b = request.args.get('word_a'), request.args.get('word_b')
    proximity = log_svc.get_proximity(word_a, word_b)
    return jsonify({
        'proximity': proximity
    })