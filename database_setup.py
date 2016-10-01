import sys
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Menu(Base):
	__tablename__ = "menu"
	id = Column(Integer, primary_key=True)
	name = Column(String(80),nullable=False)
	price = Column(Float,nullable=False)

class College(Base):
	__tablename__ = "college"
	id = Column(Integer, primary_key=True)
	name = Column(String(120),nullable=False)
	state = Column(String(120),nullable=False)

class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key=True)
	name = Column(String(80),nullable=False)
	mobile = Column(Integer,nullable=False)
	email = Column(String(80),nullable=False)
	password = Column(String(120),nullable=False)
	college_id = Column(Integer, ForeignKey('college.id'))
	college = relationship(College)

		

engine =create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)