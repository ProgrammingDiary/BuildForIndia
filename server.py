from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, College, Menu, User

app = Flask(__name__)

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

session = DBSession()

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)