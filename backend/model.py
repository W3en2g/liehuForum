from os import read
from sqlalchemy import Column,  VARCHAR, INT, DateTime, Enum, create_engine
from sqlalchemy.dialects.mysql import LONGTEXT , TINYINT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP, Enum
from sqlalchemy.sql import func
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
    nickName = Column(VARCHAR(255))
    level = Column(VARCHAR(6),server_default='Visito')
    dept = Column(VARCHAR(4))
    password = Column(VARCHAR(8))


# 定义对象:
class Post(Base):
    # 表的名字:
    __tablename__ = 'post'
    # 表的结构:
    postID = Column(INT, primary_key=True)
    title = Column(VARCHAR(255))
    content = Column(LONGTEXT)
    create_time = Column(DateTime,server_default=func.now())
    writterID = Column(INT)
    nice_post = Column(TINYINT,server_default='0')
    browse_count = Column(INT,server_default='0')
    thumbs_up = Column(INT,server_default='0')

# 定义对象:
class Comment(Base):
    # 表的名字:
    __tablename__ = 'comment'
    # 表的结构:
    commentID = Column(INT, primary_key=True)
    postID = Column(INT)
    writterID = Column(INT)
    content = Column(VARCHAR(255))
    create_time = Column(DateTime,server_default=func.now())


# 定义对象:
class TaRelation(Base):
    # 表的名字:
    __tablename__ = 'tadistribution'
    # 表的结构:
    name = Column(VARCHAR(4), primary_key=True)
    TAname = Column(VARCHAR(4))

# 定义对象:
class TaIntention(Base):
    # 表的名字:
    __tablename__ = 'ta_choosing'
    # 表的结构:
    member_num = Column(INT, primary_key=True)
    ta_num = Column(INT, primary_key=True)






