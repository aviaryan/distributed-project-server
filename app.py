import logging
import os

from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG', 'config.LocalConfig'))

# Logger
logger = logging.getLogger('hapramp_logger')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(relativeCreated)6d %(threadName)s %(message)s'
))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# import views below
