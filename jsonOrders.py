from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, College, Menu, User, Order_Details
import simplejson

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

def serialize(item):
	return {
		'OrderID': item.orderID,
		'Dish Name': item.dish.name,
		'Quantity': item.quantity,
		'Price': item.dish.price
	}

orders = session.query(Order_Details).all()

orderdict = [serialize(order) for order in orders]
print orderdict

with open("order.json", "w") as outfile:
	simplejson.dump(orderdict,outfile)
