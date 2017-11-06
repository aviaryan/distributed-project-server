import os
import json


def load_data():
    arr = os.listdir('data')
    ret = []
    for i in arr:
        fp = open('data/' + i, 'r')
        data = fp.read()
        fp.close()
        ret.append(json.loads(data))
    return ret
