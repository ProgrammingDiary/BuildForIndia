from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, College, Menu, User, Order, Order_Details

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

order1 = session.query(Order_Details).group_by(Order_Details.orderID)
for o in order1:
	print o.id
	print o.orderID
	print o.dish.name
	print o.dish.price
	print o.quantity
	print