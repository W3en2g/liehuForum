from flask import Flask, request, jsonify
from dbInterface import *
from app import app

@app.route("/liehuer/choosingTas",methods=['POST'])
def chosseTa():
    memName = request.form['memName']
    ta1Name = request.form['ta1Name']
    ta2Name = request.form['ta2Name']

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