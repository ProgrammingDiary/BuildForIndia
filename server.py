from flask import Flask, render_template, request
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

@app.route('/registeruser', methods=['GET', 'POST'])
def registerUser():
	if request.method == 'POST':
		college_id = session.query(College).filter_by(name=request.form['collegeNames']).one().id
		newUser = User(name=request.form['fullname'], mobile=request.form['mobileno'], email=request.form['email'], college_id=college_id)
		session.add(newUser)
		session.commit()
		if session.query(User).filter_by(email=request.form['email']).count() != 0:
			flash("User already registered.")
			return redirect(url_for('registerUser'))
		else:
			flash("Registration Successfull")
			return redirect(url_for('home'))
	else:
		return render_template('registerUser.html')

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8080)