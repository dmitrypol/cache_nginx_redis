''' app initializer  '''
import time
import logging
from flask import Flask, jsonify, request
from flask_caching import Cache
import requests


APP = Flask(__name__)
APP.config.from_pyfile('config.py')
CACHE = Cache(APP)


@APP.route('/')
@CACHE.cached()
def root():
    time.sleep(5)
    logging.info('api1')
    return jsonify({'api': 'one'})


@APP.route('/hello')
@CACHE.cached(timeout=120, query_string=True)
def hello():
    time.sleep(5)
    name = request.args.get('name', 'world')
    logging.info(name)
    return name


@APP.route('/getapi2')
def getapi2():
    #api2_url = 'http://api2:8080'
    api2_url = 'http://nginx/api2/'
    resp = requests.get(api2_url)
    logging.info(resp)
    return resp.text