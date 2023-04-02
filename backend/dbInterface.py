from sqlalchemy.sql.expression import and_
from model import *
from sqlalchemy.exc import IntegrityError, DataError
import re #for getting the error message
from sqlalchemy import or_

erPattern = re.compile('column(.+)at')

def addNewUser(newStuNum,newStuName,newLevel,newDept,newPassword):
    session = DBSession()
    try:
        new_liehuer = Liehuer(stuNum = newStuNum,stuName = newStuName,level = newLevel,dept = newDept,password = newPassword)
        session.add(new_liehuer)
        session.commit()
    except DataError as dateErr:# wrong input format
        raise dateErr

    except IntegrityError:
        raise Exception("该用户已注册, 请联系管理员")
    #关闭session:
    finally:
        session.close()



# def checkID_Password(hisNum,hisPassword):
#     session = DBSession()
#     queryList = session.query(Liehuer).filter(Liehuer.stuNum==hisNum).all()
#     session.close()
#     if len(queryList)==0:
#         return [False,]
#     if queryList[0].password==(hisPassword):
#         return [True,queryList[0].stuName]
#     else:
#         print(queryList[0].password)
#         return [True,queryList[0].stuName]

def checkID_Password(hisNum,hisPassword):
    session = DBSession()
    queryList = session.query(Liehuer).filter(Liehuer.stuNum==hisNum).all()
    session.close()
    if len(queryList)==0:
        return [False,'']
    if queryList[0].password==(hisPassword):
        return [True,queryList[0].stuName]
    else:
        return [False,queryList[0].stuName]



def selectTas(memName,taName):
    session = DBSession()
    member = session.query(Liehuer).filter(and_(Liehuer.stuName==memName),or_(Liehuer.level=='Junior',Liehuer.level=='Member')).one_or_none()
    ta = session.query(Liehuer).filter(Liehuer.stuName==taName, Liehuer.level=='Senior').one_or_none()
    if member is None or ta is None:
        raise Exception("没这儿人")
    try:
        newIntention = TaIntention(member_num = member.stuNum, ta_num = ta.stuNum)
        session.add(newIntention)
        session.commit()
    except DataError as dateErr:# wrong input format
        raise dateErr

    except IntegrityError:
        raise Exception("该意向以提交,请勿重复填写")
    #关闭session:
    finally:
        session.close()

def getPost(pid):
    session = DBSession()
    thePost = session.query(Post).filter(Post.postID==pid).one()
    writter = session.query(Liehuer).filter(Liehuer.stuNum==thePost.writterID).one().nickName
    session.close()
    print(thePost.content)
    return thePost.title, writter, thePost.content

def getComment(pid):
    session = DBSession()
    theCommentList = session.query(Comment).filter(Comment.postID==pid).order_by(Comment.create_time).all()
    resCommentList = []
    for i in (0,len(theCommentList)-1):
        writter = session.query(Liehuer).filter(Liehuer.stuNum==theCommentList[i].writterID).one().nickName
        currentComment = {'writter':writter, 'content':theCommentList[i].content, 'createTime':theCommentList[i].create_time}
        resCommentList.append(currentComment)
    session.close()

    return resCommentList


def create_post(newTitle,theWritterID,newContent):
    session = DBSession()
    try:
        new_post = Post(title = newTitle, writterID = theWritterID, content = newContent)
        session.add(new_post)
        session.commit()
    except Exception:
        raise Exception("提交帖子出错")
    #关闭session:
    finally:
        session.close()



def create_comment(rePostID,theWritterID,newContent):
    session = DBSession()
    try:
        new_comment = Comment(postID = rePostID, writterID = theWritterID, content = newContent)
        session.add(new_comment)
        session.commit()
    except Exception:
        raise Exception("提交评论出错")
    #关闭session:
    finally:
        session.close()

