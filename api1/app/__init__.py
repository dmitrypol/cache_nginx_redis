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
    logging.info('api1')
    return 'api1'


@APP.route('/api2')
def api2():
    #api2_url = 'http://api2:5002'
    api2_url = 'http://nginx/api2/'
    req = requests.get(api2_url)
    logging.info(req)
    return req.text