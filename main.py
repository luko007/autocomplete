import redis
from flask import Flask, request, jsonify

app = Flask(__name__)

PREFIX = '_'
TERMINAL = '+'
db = redis.StrictRedis()
numOfSuggestions = 50

@app.route("/store", methods=['POST'])
def store() -> str:
    key = PREFIX
    pipeline = db.pipeline(True)
    word = request.args.get('word')
    for c in word:
        key += c
        a = db.zadd(key, {word: 0})
        if not a:
            return "No elements were added"
    # db.zadd(key, TERMINAL, 0)
    pipeline.execute()
    return "Success!"

@app.route("/suggest")
def suggest():
    word = request.args.get('word', type=str)
    return jsonify(suggestWord(word))


def suggestWord(word):
    results = []
    for c in db.zrange(PREFIX + word, 0, numOfSuggestions):
        c = c.decode('UTF-8')
        results.append(c)
    return results

if __name__ == "__main__":
    app.run()