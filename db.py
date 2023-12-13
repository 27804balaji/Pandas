import pandas as p
import sqlalchemy as s
db = s.create_engine('mysql+pymysql://root:@localhost:14600/db_1')
data = p.read_sql_table('student',db,schema=None)
print(data)