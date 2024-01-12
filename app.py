from flask import Flask, request, jsonify
from db import db
from Models import *

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


# create tables
with app.app_context():
    db.create_all()


@app.route("/basket", methods=["POST"])
def add_to_basket():
    user_id = int(request.form.get("user_id"))
    item_id = int(request.form.get("item_id"))
    new_record = Basket(user_id=user_id, item_id=item_id)
    db.session.add(new_record)
    db.session.commit()
    return "Added", 201

@app.route("/basket/<user_id>", methods=["GET"])
def get_basket(user_id):
    basket = db.session.query(Basket).filter_by(user_id=user_id)
    output = []
    for record in basket:
        output.append({"item_id": record.item_id, "item_name":record.item.name})
    return jsonify(output)


@app.route("/users", methods=["POST"])
def add_user():
    name = request.form.get("username")
    new_item = Users(username=name, password="")
    db.session.add(new_item)
    db.session.commit()
    return "Added", 201


@app.route("/users", methods=["GET"])
def get_users():
    users = db.session.query(Users)
    output = []
    for user in users:
        output.append({"user_id":user.id, "user_name":user.username})
    return jsonify(output), 200



@app.route("/items", methods=["POST"])
def add_item():
    name = request.form.get("name")
    new_item = Item(name=name)
    db.session.add(new_item)
    db.session.commit()
    return "Added", 201


@app.route("/items", methods=["GET"])
def get_items():
    items = db.session.query(Item)
    output = []
    for item in items:
        output.append({"item_id":item.id, "item_name":item.name})
    return jsonify(output), 200

@app.route("/items/<id>", methods=["DELETE"])
def delete_item(id):
    item = db.get_or_404(Item, id)
    db.session.delete(item)
    db.session.commit()
    return "Deleted", 200

if __name__ == '__main__':  
   app.run(host='0.0.0.0', port=2900)