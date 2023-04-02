
# 数据库连接:
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://liehuer:liehu2019@120.25.206.240:3306/liehuforum')
# engine = create_engine('mysql+pymysql://liehuer:liehu2019@localhost:3306/liehuforum')