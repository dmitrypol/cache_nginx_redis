''' app initializer  '''
import time
import os
import logging
from flask import Flask
from flask_caching import Cache


APP = Flask(__name__)
APP.config.from_pyfile('config.py')
CACHE = Cache(APP)


@APP.route('/')
@CACHE.cached()
def root():
    time.sleep(10)
    logging.info('root')
    return 'root'
