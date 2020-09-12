''' app initializer  '''
import time
import logging
from flask import Flask
from flask_caching import Cache
import requests


APP = Flask(__name__)
APP.config.from_pyfile('config.py')
CACHE = Cache(APP)


@APP.route('/')
@CACHE.cached()
def root():
    time.sleep(10)
    logging.info('api2')
    return 'api2'


@APP.route('/api1')
def api1():
    #api1_url = 'http://api1:5001'
    api1_url = 'http://nginx/api1/'
    req = requests.get(api1_url)
    logging.info(req)
    return req.text