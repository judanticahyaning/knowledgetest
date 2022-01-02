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

    return redirect(url_for('index'))

@app.route('/editFilm/<id>', methods=['PUT'])
def editFilm(id):

    return jsonify("berhasil")

@app.route('/delFilm/<id>',methods=['DELETE'])
def delFilm(id):
    sql = engine.execute("DELETE FROM film WHERE id=" + id)
    response = {"msg": "berhasil dihapus"}
    return response
