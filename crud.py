from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# username = 'postgres'
# password = 'vinay'
# dbname='localhost:5432/newdb'

db = create_engine('postgresql+pg8000://postgres:vinay@localhost/testdb')

# db = create_engine(db_string)
base = declarative_base()

class Film(base):
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Create
doctor_strange = Film(title="Doctor Strange", director="Scott Derrickson", year="2016")
session.add(doctor_strange)
session.commit()

# Read
films = session.query(Film)
for film in films:
    print(film.title)

# Update
doctor_strange.title = "Some2016Film"
for film in films:
    print(film.title)
session.commit()

# Delete
session.delete(doctor_strange)
session.commit()