from flask import Flask, request, jsonify
from flask.wrappers import Request
import json

from sqlalchemy.sql.elements import Null
from sqlalchemy.exc import IntegrityError 
from pymysql.err import IntegrityError as ierror
from dbInterface import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/liehuer/register",methods=['POST'])
def register():
    stuNum = request.form['stuNum']
    stuName = request.form['stuName']
    password = request.form['password']

    try:
        addNewUser(stuNum,stuName,'Visito','',password)
    except Exception:
        return "你已注册,请和管理员联系"
    return "hello"+ stuName + " , 你已注册"

@app.route("/liehuer/login",methods=['POST'])
def login():
    stuNum = request.form['stuNum']
    password = request.form['password']
    stuNum = int(stuNum)
    password = str(password)
    loginRes = checkID_Password(stuNum,password)
    if loginRes[0]:
        loginName = loginRes[1]
        return "hello"+ loginName + " , 你已登录"
    elif loginRes[1]=='':
        return "查无此人"
    else:
        return "<p>wrong password</p>"