from app import app
from flask import request, jsonify
from utils import load_data


channels = {}
channel_members = {}
all_data = load_data()


@app.route('/')
def home():
    return 'Project running'


@app.route('/channels/<name>', methods=['POST'])
def create_channel(name):
    channels[name] = {'count': 0, 'search': None, 'results': {}, 'result_count': 0}
    return jsonify({'status': 'ok'})


@app.route('/channels/<name>', methods=['DELETE'])
def delete_channel(name):
    del channels[name]
    return jsonify({'status': 'ok'})


@app.route('/channels')
def list_channels():
    return jsonify(channels)


@app.route('/join_channel/<name>', methods=['POST'])
def join_channel(name):
    channels[name]['count'] += 1
    return jsonify({'status': 'ok', 'id': channels[name]['count']})


@app.route('/leave_channel/<name>', methods=['POST'])
def leave_channel(name):
    channels[name]['count'] -= 1
    return jsonify({'status': 'ok'})


@app.route('/set_search/<name>/<term>', methods=['POST'])
def set_search(name, term):
    channels[name]['search'] = term
    channels[name]['result_count'] = 0
    channels[name]['results'] = {}
    return jsonify({'status': 'ok'})


@app.route('/get_search/<name>')
def get_search(name):
    return jsonify({'search': channels[name]['search']})


@app.route('/upload_search/<name>/<id>', methods=['POST'])
def upload_search(name, id):
    channels[name]['results'] = request.data  # merge here
    channels[name]['result_count'] += 1
    return jsonify({'status': 'ok'})


@app.route('/get_result/<name>')
def get_result(name):
    if channels[name]['result_count'] < channels[name]['count']:
        return jsonify({'status': 'waiting'})
    return jsonify({'status': 'ok', 'results': channels[name]['results']})


@app.route('/download_data/<name>/<id_>', methods=['POST'])
def download_data(name, id_):
    x = len(all_data)
    div = int(x / channels[name]['count'])
    print('div', div)
    return jsonify({'results': all_data[(int(id_) - 1) * div : div]})
