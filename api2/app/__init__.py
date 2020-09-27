''' app initializer  '''
import time
import logging
from flask import Flask, jsonify
from flask_caching import Cache
import requests


APP = Flask(__name__)
APP.config.from_pyfile('config.py')
CACHE = Cache(APP)


@APP.route('/')
@CACHE.cached()
def root():
    time.sleep(5)
    logging.info('api2')
    return jsonify({'api': 'two'})


@APP.route('/getapi1')
def getapi1():
    #api1_url = 'http://api1:5001'
    api1_url = 'http://nginx/api1/'
    resp = requests.get(api1_url)
    logging.info(resp)
    return resp.text