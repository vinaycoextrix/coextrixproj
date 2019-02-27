import sqlalchemy
from sqlalchemy import create_engine
print(sqlalchemy.__version__ )

engine = create_engine('sqlite:///:memory:', echo=True)


