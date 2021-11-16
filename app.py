from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo-svc")
db = client.dbKuber


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/memo', methods=['POST'])
def save_post():
    params = request.get_json()

    post = {
        'title': params['title'],
        'content': params['content'],
    }
    db.memo.insert_one(post)
    return jsonify({"result": "success"})


if __name__ == '__main__':
    app.run()
