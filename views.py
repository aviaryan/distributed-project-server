from app import app
from flask import request, jsonify


channels = []


@app.route('/')
def home():
    return 'Project running'


@app.route('/channels/<name>', methods=['POST'])
def create_channel(name):
    channels.append(name)
    return jsonify({'status': 'ok'})


@app.route('/channels')
def list_channels():
    return jsonify({'channels': channels})
