from app import app
from flask import request, jsonify


channels = {}
channel_members = {}


@app.route('/')
def home():
    return 'Project running'


@app.route('/channels/<name>', methods=['POST'])
def create_channel(name):
    channels[name] = {'count': 0}
    return jsonify({'status': 'ok'})


@app.route('/channels')
def list_channels():
    return jsonify(channels)


@app.route('/join_channel/<name>', methods=['POST'])
def join_channel(name):
    channels[name]['count'] += 1
    return jsonify({'status': 'ok'})


@app.route('/leave_channel/<name>', methods=['POST'])
def leave_channel(name):
    channels[name]['count'] -= 1
    return jsonify({'status': 'ok'})
