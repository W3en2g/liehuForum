from flask import Flask, request, jsonify
from dbInterface import *
from app import app


@app.route("/api/createpost",methods=['POST'])
def post_create():
    title = request.form['postTitle']
    writterID = request.form['writterID']
    content = request.form['postContent']
    create_post(title,writterID,content)
    return content

@app.route("/api/createcomment",methods=['POST'])
def comment_create():
    postID = request.form['postID']
    writterID = request.form['writterID']
    content = request.form['commentContent']
    create_comment(postID,writterID,content)
    return content

@app.route("/api/getpost",methods=['get'])
def post_get():
    postID = request.args['pid']
    title,writter,content = getPost(postID)
    return jsonify({'title': title, 'writter':writter,'content': content})
 
@app.route("/api/getcomment",methods=['get'])
def comment_get():
    postID = request.args['pid']
    resCommentList = getComment(postID)
    return jsonify({'len': len(resCommentList), 'resCommentList':resCommentList})