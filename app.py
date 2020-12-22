from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json



app=Flask(__name__)
app.secret_key='super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cart'
db = SQLAlchemy(app)

date=datetime.now()
user="deepak"
pas="foxy"

class items(db.Model):    
    sno=db.Column(db.Integer,nullable=False,primary_key=True)
    cart_product_id=db.Column(db.String(20),nullable=False)
    cart_quantity = db.Column(db.Integer, primary_key=True)
    cart_image = db.Column(db.String(30), nullable=False)
    cart_price = db.Column(db.Integer, nullable=False)

@app.route('/', methods=['GET','POST'])
def hom():
    return render_template("layout.html")

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template("layout1.html")

@app.route('/cart', methods=['GET','POST'])
def cart():
    if ('user' in session and session['user'] == user):
        item = items.query.all()
    else:
        return redirect('/login')
    return render_template("cart.html",date=date,item = item)

@app.route('/delete/<string:sno>')
def delete1(sno):
    item = items.query.filter_by(sno=sno).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/cart")

@app.route('/login', methods=['GET','POST'])
def login():
    if('user' in session and session['user']==user):
        return redirect('/home')
    elif (request.method=='POST'):
        username=request.form.get('user')
        password=request.form.get('pass')
        if(username==user and password==pas):
            session['user']=username
            return redirect("/home")

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/mobiles', methods=['GET','POST'])
def mobiles():
    return render_template("mobiles.html")

@app.route('/one-plus', methods=['GET','POST'])
def oneplus():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="one-plus",cart_quantity=quantity,cart_image="../static/one-plus.jpg",cart_price=49999)
        db.session.add(item)
        db.session.commit()
    return render_template("one-plus.html")

@app.route('/iphone', methods=['GET','POST'])
def iphone():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="iphone",cart_quantity=quantity,cart_image="../static/iphone.jpg",cart_price=94999)
        db.session.add(item)
        db.session.commit()
    return render_template("iphone.html")

@app.route('/samsung', methods=['GET','POST'])
def samsung():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="samsung",cart_quantity=quantity,cart_image="../static/samsung.jpg",cart_price=74999)
        db.session.add(item)
        db.session.commit()
    return render_template("samsung.html")

@app.route('/clothes', methods=['GET','POST'])
def clothes():
    return render_template("clothes.html")

@app.route('/blazer', methods=['GET','POST'])
def blazer():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="blazer",cart_quantity=quantity,cart_image="../static/blazer.jpg",cart_price=3999)
        db.session.add(item)
        db.session.commit()
    return render_template("blazer.html")

@app.route('/trouser', methods=['GET','POST'])
def trouser():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="trouser",cart_quantity=quantity,cart_image="../static/trouser.jpeg",cart_price=1999)
        db.session.add(item)
        db.session.commit()
    return render_template("trouser.html")

@app.route('/shoes', methods=['GET','POST'])
def shoes():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="shoes",cart_quantity=quantity,cart_image="../static/shoes.jpg",cart_price=4999)
        db.session.add(item)
        db.session.commit()
    return render_template("shoes.html")

@app.route('/television', methods=['GET','POST'])
def television():
    return render_template("television.html")


@app.route('/lg-tv', methods=['GET','POST'])
def lgtv():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="lg-tv",cart_quantity=quantity,cart_image="../static/lg-tv.jpg",cart_price=139999)
        db.session.add(item)
        db.session.commit()
    return render_template("lg-tv.html")

@app.route('/samsung-tv', methods=['GET','POST'])
def samsungtv():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="samsung-tv",cart_quantity=quantity,cart_image="../static/samsung-tv.jpg",cart_price=149999)
        db.session.add(item)
        db.session.commit()
    return render_template("samsung-tv.html")

@app.route('/sony-tv', methods=['GET','POST'])
def sonytv():
    if (request.method=='POST'):
        quantity=request.form.get("quantity")
        item = items(cart_product_id="sony-tv",cart_quantity=quantity,cart_image="../static/sony-tv.jpg",cart_price=109999)
        db.session.add(item)
        db.session.commit()
    return render_template("sony-tv.html")

@app.route('/check-out')
def checkout():
    item = items.query.all()
    a=0
    b=0
    for i in item:
        a = a + (i.cart_price*i.cart_quantity)
        b = b + i.cart_quantity

    l=str(a)
    n=len(l)
    if (n<=3):
        price = l
    elif (n==4):
        price = f"{l[0]},{l[1:4]}"
    elif (n==5):
        price = f"{l[0:2]},{l[2:5]}"
    elif(n==6):
        price = f"{l[0]},{l[1:3]},{l[3:6]}"
    elif(n==7):
        price = f"{l[0:2]},{l[2:4]},{l[4:7]}"
    elif(n==8):
        price=f"{l[0]},{l[1:3]},{l[3:5]},{l[5:8]}"
    
    quantity=b
    return render_template("checkout.html",price=price,quantity=quantity)

if __name__ == "__main__":
    app.run(debug=True)