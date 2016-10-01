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
		'price': item.price,
	}

menus = session.query(Menu).all()

menudict = [serialize(menu) for menu in menus]
print menudict

with open("menu.json", "w") as outfile:
	simplejson.dump(menudict,outfile)