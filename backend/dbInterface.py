from model import DBSession, Liehuer, TaRelation
from sqlalchemy.exc import IntegrityError

def addNewUser(newStuNum,newStuName,newLevel,newDept,newPassword):
    session = DBSession()
    try:
        new_liehuer = Liehuer(stuNum = newStuNum,stuName = newStuName,level = newLevel,dept = newDept,password = newPassword)
        session.add(new_liehuer)
        session.commit()
    except Exception:
        raise Exception
    # 关闭session:
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
    
