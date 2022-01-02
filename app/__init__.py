from flask import Flask, request

app = Flask (__name__, template_folder='template')

from app.module.controller import *
from app.module.api import *

app.secret_key = "judanticahyaning"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/knowledge_test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

