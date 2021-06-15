import redis
from flask import Flask, request, jsonify
import pandas as pd
import time

app = Flask(__name__)

PREFIX = '_'
TERMINAL = '+'
db = redis.StrictRedis()
NUM_OF_SUGGESTIONS = 50

@app.route("/store", methods=['POST'])
def store() -> str:
    word = request.args.get('word')
    storeWord(word, 0)
    return "Success!"

def storeWord(word: str, score: int):
    key = PREFIX
    pipeline = db.pipeline(True)
    for c in word:
        key += c
        a = db.zadd(key, {word: score})
    pipeline.execute()


@app.route("/suggest")
def suggest():
    word = request.args.get('word', type=str)
    return jsonify(suggestWord(word))


def suggestWord(word, numOfSuggestions = NUM_OF_SUGGESTIONS):
    results = []
    for curr_word in db.zrange(PREFIX + word, 0, numOfSuggestions, desc=True):
        curr_word = curr_word.decode('UTF-8')
        results.append(curr_word)
    return results


def add_words_to_db(csvFile):
    for _, row in csvFile.iterrows():
        storeWord(row['word'], row['count'])


def parse_csv(csv_file_name):
    with open(csv_file_name) as csv:
        pandas_csv = pd.read_csv(csv)
        pandas_csv['word'] = pandas_csv['word'].astype(str)
        pandas_csv['count'] = pandas_csv['count'].astype(float)
        pandas_csv.dropna(inplace=True)
        return pandas_csv


if __name__ == "__main__":
    # start_time = time.time()
    # pandas_csv_file = parse_csv("unigram_freq.csv")
    # add_words_to_db(pandas_csv_file)
    # print(time.time()-start_time)
    app.run()
