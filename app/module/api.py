from flask_restful import Resource, Api
from flask_cors import CORS
from app import app, request
from app.module.controller import *
from sqlalchemy import create_engine

# from app.module.model import *

api = Api(app)
CORS(app)

engine = create_engine("mysql+mysqlconnector://root@localhost:3306/knowledge_test", echo=False)
class show(Resource):
    def get(self):
        sql = engine.execute("SELECT * FROM film")
        output = [{
            "id":data.id,
            "title":data.title,
            "genre":data.genre,
            "rating":data.rating,
            "duration":data.duration,
            "quality":data.quality,
            "trailer":data.trailer,
            "watch":data.watch
        }
            for data in sql
        ]
        response = output
        return response

class add(Resource):
    def post(self):
        title = request.form['title']
        genre = request.form['genre']
        rating = request.form['rating']
        duration = request.form['duration']
        quality = request.form['quality']
        trailer = request.form['trailer']
        watch = request.form['watch']

        sql = "INSERT INTO film(title, genre, rating, duration, quality, trailer, watch) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        data = (title, genre, rating, duration, quality, trailer, watch)
        proses = engine.execute(sql, data)
        response = {"msg": "Berhasil!"}
        return response

# class edit(Resource):
#     def put(self,id):
#         # id = request.form['id']
#         title = request.form['title']
#         genre = request.form['genre']
#         rating = request.form['rating']
#         duration = request.form['duration']
#         quality = request.form['quality']
#         trailer = request.form['trailer']
#         watch = request.form['watch']
#         sql = engine.execute("UPDATE film SET title=%s, genre=%s, rating=%s, duration=%s, quality=%s, "
#                              "trailer=%s, watch=%s WHERE id=%s",
#                              (title, genre, rating, duration, quality, trailer, watch, id))
#         output = [{
#                      "id":data.id,
#                      "title":data.title,
#                      "genre":data.genre,
#                      "rating":data.rating,
#                      "duration":data.duration,
#                      "quality":data.quality,
#                      "trailer":data.trailer,
#                      "watch":data.watch
#                  }
#                      for data in sql
#                  ]
#         response ={
#              "msg" : "berhasil ditampilkan",
#              "data" : output
#
#         }
#         return response

# class delete(Resource):
#     def hapus(self, id):
#         sql = engine.execute("DELETE FROM film WHERE id=" + id)
#         response = {"msg":"berhasil dihapus"}
#         return response

api.add_resource(show, "/data", methods=["GET"])
api.add_resource(add, "/addFilm", methods=["POST"])
# api.add_resource(edit, "/editFilm/<id>", methods=["PUT"])
# yang belum bisa delete
# api.add_resource(delete, "/delFilm/<id>", methods=["DELETE"])