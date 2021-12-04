from flask import render_template, request, redirect
from app import app
from models.item import *
from models.items import items,add_new_item,delete_item


@app.route('/items')
def index():
    return render_template("index.html",title = "Shoping List Items", items=items)

# 
@app.route('/items', methods =['post'])
# add_item() can be anyname.
def add_item():
    name_of_item = request.form['name_of_item']
    price = request.form['price']
    quantity = request.form['quantity']
    Bought_status = True if 'Bought_status' in request.form else False

    new_item = Item(name_of_item=name_of_item,price=price,quantity=quantity,Bought_status=Bought_status)    

    add_new_item(new_item)
    # both are working
    # return render_template("index.html",title = "Shoping List Items", items=items)
    return redirect('/items')

@app.route('/items/delete/<name_of_item>', methods=['POST'])
def delete(name_of_item):
  delete_item(name_of_item)
  return redirect('/items')
