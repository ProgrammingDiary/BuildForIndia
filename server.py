from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, College, Menu, User, Merchant


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
		newUser = User(name=request.form['fullname'], mobile=request.form['mobileno'], email=request.form['email'], college_id=college_id,password=request.form['password'])
		session.add(newUser)
		session.commit()
		if session.query(User).filter_by(email=request.form['email']).count() != 0:
			flash("User already registered.")
			return redirect(url_for('registerUser'))
		else:
			flash("Registration Successfull")
			return redirect('/')
	else:
		return render_template('registerUser.html')

@app.route('/registermerchant', methods=['GET', 'POST'])
def registerMerchant():
	if request.method == 'POST':
		newUser = Merchant(name=request.form['fullname'], mobile=request.form['mobileno'], email=request.form['email'],address=request.form['address'],company=request.form['company'],password=request.form['password'])
		session.add(newUser)
		session.commit()
		if session.query(Merchant).filter_by(email=request.form['email']).count() != 0:
			flash("Merchant already registered.")
			return redirect(url_for('registerMerchant'))
		else:
			flash("Registration Successfull")
			return redirect('/')
	else:
		return render_template('merchantRegister.html')

@app.route('/userlogin', methods=['GET', 'POST'])
def loginUser():
	if request.method == 'POST':
		userQuery = session.query(User).filter_by(email=request.form['email'])
		currUser = userQuery.one()
		if userQuery.count() == 0:
			flash("Invalid Account")
			return redirect('/userlogin')
		else:	
			if currUser.password == request.form['password']:
				flash("Registration Successfull")
				return redirect(url_for('Menu', userid=currUser.id), code=200)
			else:
				flash("Invalid Credentials")
				return redirect('/userlogin')
	else:
		return render_template('loginUser.html')

@app.route('/merchantlogin', methods=['GET', 'POST'])
def loginMerchant():
	if request.method == 'POST':
		userQuery = session.query(Merchant).filter_by(email=request.form['email'])
		currUser = userQuery.one()
		if userQuery.count() == 0:
			flash("Invalid Account")
			return redirect('/merchantlogin')
		else:
			if currUser.password == request.form['password']:
				flash("Registration Successfull")
				return redirect('/')
			else:
				flash("Invalid Credentials")
				return redirect('/merchantlogin')
	else:
		return render_template('loginMerchant.html')

@app.route('/dashboard/<userid>', methods=['GET', 'POST'])
def Menu(userid):
	if request.method == 'POST':
		print request.args.get('Shahi Paneer',0,type=int)

		Amount = (request.form['Shahi Paneer']*180) + (request.form['Burger']*30) + (request.form['Pav Bhaji']*50000)
		newOrder = Order(userID=userid, Amount=Amount)
		session.add(Order(newOrder))
		session.commit()
		order_1 = Order_Details(orderID=newOrder.id,quantity=request.form['Shahi Paneer'],dishID=session.query(Menu).filter_by(name='Shahi Paneer').one().id)
		order_2 = Order_Details(orderID=newOrder.id,quantity=request.form['Burger'],dishID=session.query(Menu).filter_by(name='Burger').one().id)
		order_3 = Order_Details(orderID=newOrder.id,quantity=request.form['Pav Bhaji'],dishID=session.query(Menu).filter_by(name='Pav Bhaji').one().id)
		session.add(Order_Details(order_1))
		session.commit()
		session.add(Order_Details(order_2))
		session.commit()
		session.add(Order_Details(order_3))
		session.commit()
		if Amount == 0:
			flash("Please Enter valid quantities")
			return redirect('/merchantlogin')
		else:
			flash("Registration Successfull")
			return redirect('/')
			
	else:
		return render_template('Menu.html')

#@app.route('/response.cgi')
#def Response():
#	return response

if __name__ == '__main__':
	app.debug = True
	app.secret_key = 'some_secret'
	app.run(host='0.0.0.0', port=8080)