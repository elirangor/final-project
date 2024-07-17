import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
#Testing
app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI","mongodb://root:root@my-mongodb-release:27017/")
client = MongoClient(MONGO_URI)  # Update with your MongoDB URI
#client = MongoClient('mongodb://mongo:27017/')
db = client.mydatabasetest  # Replace 'mydatabase' with your database name
collection = db.mycollectiontest  # Replace 'mycollection' with your collection name


@app.route('/')
def index():
    documents = list(collection.find())
    for document in documents:
        document['_id'] = str(document['_id'])
    return render_template('index.html', documents=documents)

@app.route('/add', methods=['POST'])
def add_document():
    data = request.form.to_dict()
    collection.insert_one(data)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_document():
    id = request.form.get('id')
    data = request.form.to_dict()
    del data['id']
    collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_document():
    id = request.form.get('id')
    collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)