from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, College, Menu, User

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

session.add(College(name = "IIT Delhi", state = "Delhi"))
session.commit()
session.add(College(name = "IIT Bombay", state = "Maharashtra"))
session.commit()
session.add(College(name = "IIT Guwahati", state = "Assam"))
session.commit()
session.add(College(name = "IIT Roorkee", state = "Uttarakhand"))
session.commit()
session.add(College(name = "IIT Kharagpur", state = "West Bengal"))
session.commit()
session.add(College(name = "IIT Dhanbad", state = "Jharkhand"))
session.commit()