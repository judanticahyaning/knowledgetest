from flask import Flask, request

app = Flask (__name__, template_folder='template')

from app.module.controller import *
from app.module.api import *
from app.module.model import *

app.secret_key = "judanticahyaning"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/knowledge_test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# identitas = {}
#
# class ContohResouce(Resource):
#     def get(self):
#         response = {"msg":"Hello World!"}
#         return identitas
#     def post(self):
#         title = request.form['title']
#         genre = request.form['genre']
#         identitas["title"] = title
#         identitas["genre"] = genre
#         # rating = request.form['rating']
#         # duration = request.form['duration']
#         # quality = request.form['quality']
#         # trailer = request.form['trailer']
#         # watch = request.form['watch']
#         response = {"msg": "Berhasil!"}
#         return response
#
# api.add_resource(ContohResouce, "/api", methods=["GET", "POST"])
