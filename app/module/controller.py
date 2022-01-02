from app import app
from flask import render_template, url_for, request, redirect, make_response
from app.module.api import *
from sqlalchemy import create_engine
from flask import jsonify

from app.module.api import api

engine = create_engine("mysql+mysqlconnector://root@localhost:3306/knowledge_test", echo=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addFilm', methods=['POST'])
def addFilm():
    # if request.method == "POST":
    #     api.add_resource(add, "/addFilms", methods=["POST"])
    # title = request.form['title']
    # genre = request.form['genre']
    # rating = request.form['rating']
    # duration = request.form['duration']
    # quality = request.form['quality']
    # trailer = request.form['trailer']
    # watch = request.form['watch']
    #
    # sql = "INSERT INTO film(title, genre, rating, duration, quality, trailer, watch) VALUES (%s, %s, %s, %s,%s,%s,%s)"
    # data = (title, genre, rating, duration, quality, trailer, watch)
    # proses = engine.execute(sql, data)
    return redirect(url_for('index'))

@app.route('/editFilm/<id>', methods=['PUT'])
def editFilm(id):
    title = request.form['title']
    genre = request.form['genre']
    rating = request.form['rating']
    duration = request.form['duration']
    quality = request.form['quality']
    trailer = request.form['trailer']
    watch = request.form['watch']
    sql = engine.execute("UPDATE film SET title=%s, genre=%s, rating=%s, duration=%s, quality=%s, "
                         "trailer=%s, watch=%s WHERE id=%s",
                         (title, genre, rating, duration, quality, trailer, watch, id))
    # api.add_resource(edit, "/editFilm/<id>", methods=["PUT"])
    # return redirect(url_for('index'))
    return jsonify("berhasil")

@app.route('/delFilm/<id>',methods=['DELETE'])
def delFilm(id):
    sql = engine.execute("DELETE FROM film WHERE id=" + id)
    response = {"msg": "berhasil dihapus"}
    return response
