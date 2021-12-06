from os import read
from sqlalchemy import Column,  VARCHAR, CHAR, INT, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
engine = create_engine('mysql+pymysql://root:mysql@localhost:3306/liehuer')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()


# 定义对象:
class liehuer(Base):
    # 表的名字:
    __tablename__ = 'liehuer'
    # 表的结构:
    stuName = Column(VARCHAR(4), primary_key=True)
    level = Column(CHAR(6))
    dept = Column(CHAR(3))
    grade = Column(INT)

# 定义对象:
class TaRelation(Base):
    # 表的名字:
    __tablename__ = 'tadistribution'
    # 表的结构:
    name = Column(VARCHAR(4), primary_key=True)
    TAname = Column(VARCHAR(4))






    # def add(self):
    #     # 创建新User对象:
    #     new_user = User(stuName='冯境', level='Senior',dept = 'MDA', grade = '20')
    #     # 添加到session:
    #     self.session.add(new_user)
    #     # 提交即保存到数据库:
    #     self.session.commit()
    
    # def read(self):
    #     # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    #     user = self.session.query(User).filter(User.stuName=='aaa').one()
    #     # 打印类型和对象的name属性:
    #     print('type:', type(user))
    #     print('name:', user.stuName)
