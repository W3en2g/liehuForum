from flask import Flask, request, jsonify
from dbInterface import *
from app import app


@app.route("/liehuer/signup",methods=['POST'])
def signup():
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

