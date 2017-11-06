import os


def load_data():
    arr = os.listdir('data')
    ret = []
    for i in arr:
        fp = open('data/' + i, 'r')
        data = fp.read()
        fp.close()
        ret.append(data)
    return ret
