
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
    return render_template("iphone.html")
