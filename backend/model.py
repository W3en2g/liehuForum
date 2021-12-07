from os import read
from sqlalchemy import Column,  VARCHAR, CHAR, INT, Enum, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Enum

# set the connection in the model, outer file just need to end the connection
# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:mysql@localhost:3306/liehuer')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# # 创建session对象:
# session = DBSession()

# 定义对象:
class Liehuer(Base):
    # 表的名字:
    __tablename__ = 'liehuer'
    # 表的结构:
    stuNum = Column(INT, primary_key=True)
    stuName = Column(VARCHAR(4))
    level = Column(VARCHAR(6))
    dept = Column(VARCHAR(4))
    password = Column(VARCHAR(8))

# 定义对象:
class TaRelation(Base):
    # 表的名字:
    __tablename__ = 'tadistribution'
    # 表的结构:
    name = Column(VARCHAR(4), primary_key=True)
    TAname = Column(VARCHAR(4))






