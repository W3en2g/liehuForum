from flask import Flask, request, jsonify
from flask.wrappers import Request
import json

from sqlalchemy.sql.elements import Null
from sqlalchemy.exc import IntegrityError 
from pymysql.err import DataError 
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
    # addNewUser(stuNum,stuName,'Visito','',password)
    try:
        addNewUser(stuNum,stuName,'Visito','',password)

    except DataError as dateErr:
        erResult = erPattern.findall(str(dateErr.args))
        errMessa = erResult[len(erResult)-1] [3:-3]
        return errMessa+"的填写有问题"

    except Exception as Ex:
        return str(Ex)
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


@app.route("/liehuer/choosingTas",methods=['POST'])
def chosseTa():
    memName = request.form['memName']
    ta1Name = request.form['ta1Name']
    ta2Name = request.form['ta2Name']

    # 未处理异常
    try:
        selectTas(memName,ta1Name)
        selectTas(memName,ta2Name)
    except DataError as dateErr:
        erResult = erPattern.findall(str(dateErr.args))
        errMessa = erResult[len(erResult)-1] [3:-3]
        return errMessa+"的填写有问题"

    except Exception as Ex:
        return str(Ex)
    return "你已经选择"

 