from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import json
import pytz

app = Flask(__name__)
client = MongoClient('mongodb+srv://hrithik:<password>@cluster5.ktn8tna.mongodb.net/Webhook?retryWrites=true&w=majority&appName=Cluster5')
db = client.webhook_db

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Convert timestamp to datetime object
    data['timestamp'] = datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
    # Insert data into MongoDB
    db.actions.insert_one(data)
    return jsonify({'status': 'success'}), 200

@app.route('/')
def index():
    # Fetch latest actions from MongoDB
    actions = db.actions.find().sort('timestamp', -1).limit(10)
    formatted_actions = []
    for action in actions:
        action['_id'] = str(action['_id'])  # Convert ObjectId to string
        action['timestamp'] = action['timestamp'].replace(tzinfo=pytz.utc).strftime('%d %B %Y - %I:%M %p UTC')
        formatted_actions.append(action)
    return render_template('index.html', actions=formatted_actions)

if __name__ == '__main__':
    app.run(debug=True)
