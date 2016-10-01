from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, College, Menu, User

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

session.add(Menu(name = "Shahi Paneer", price = "180"))
session.commit()
session.add(Menu(name = "Burger", price = "30"))
session.commit()
session.add(Menu(name = "Pav Bhaji", price = "50"))
session.commit()
