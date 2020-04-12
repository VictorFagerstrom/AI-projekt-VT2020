from os import environ
from flask import Flask

APP = Flask(_name_)
APP.run(host='0.0.0.0', port=environ.get('PORT'))