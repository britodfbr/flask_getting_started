# coding: utf-8

from difflib import SequenceMatcher, get_close_matches
from flask import Flask, jsonify, request
from mongoengine import connect
from db import ClosestWordLog, ProximityLog

app = Flask(__name__)


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
    try:
        closest_word = get_close_matches(word, possibilities, n=1)[0]
    except IndexError:
        closest_word = 'No matches'
    ClosestWordLog(word=word, closest_word=closest_word).save()
    return jsonify({
        'closest_word': closest_word
    })


@app.route('/proximity', methods=('GET', ))
def proximity():
    word_a, word_b = request.args.get('word_a'), request.args.get('word_b')
    proximity = SequenceMatcher(a=word_a, b=word_b).ratio()
    ProximityLog(word=word_a, word_b=word_b, proximity=proximity).save()
    return jsonify({
        'proximity': proximity
    })


if __name__ == '__main__':
    connect('localhost:27017')
    app.run(debug=True)
