from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, College, Menu, User
import simplejson

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

def serialize(item):
	return {
		'name': item.name,
		'state': item.state,
	}

colleges = session.query(College).all()

menudict = [serialize(college) for college in colleges]
print menudict

with open("college.json", "w") as outfile:
	simplejson.dump(menudict,outfile)
