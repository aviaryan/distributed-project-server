import os
import json


def load_data():
    arr = os.listdir('data')
    ret = []
    for i in arr:
        if i == 'channels.json':
            continue
        fp = open('data/' + i, 'r')
        data = fp.read()
        fp.close()
        ret.append(json.loads(data))
    return ret


def load_channels():
    if not os.path.isfile('data/channels.json'):
        return {}
    fp = open('data/channels.json', 'r')
    data = fp.read()
    fp.close()
    return json.loads(data)


def save_channels(channels):
    data = json.dumps(channels)
    fp = open('data/channels.json', 'w')
    fp.write(data)
    fp.close()
