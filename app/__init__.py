from flask import Flask,request
from flask_restful import Api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


from .restful import *

