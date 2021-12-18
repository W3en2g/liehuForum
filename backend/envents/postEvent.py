from flask import Flask, request, jsonify
from dbInterface import *
from app import app


@app.route("/api/createpost",methods=['POST'])
def post_create():
    title = request.form['postTitle']
    writterID = request.form['writterID']
    content = request.form['postContent']
    posts_create(title,writterID,content)
    return content

@app.route("/api/getpost",methods=['get'])
def post_get():
    postID = request.args['pid']
    title,writter,content = getPost(postID)

    return jsonify({'title': title, 'writter':writter,'content': content})
