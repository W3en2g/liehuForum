from model import session, liehuer, TaRelation

reslut = session.query(liehuer).filter(liehuer.stuName=='aaa').one()
print(reslut.stuName)