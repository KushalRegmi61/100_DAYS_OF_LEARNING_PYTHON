
''''This the api documentation : https://documenter.getpostman.com/view/37746097/2sA3s9CTh5'''

from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictonary ={}
        #Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")   #GET METHOD IS ALLOWED BY DEFAULT
def get_random_cafe():
    if request.method=="GET":
        result= db.session.execute(db.select(Cafe))
        cafes= result.scalars().all()
        random_cafe = random.choice(cafes)
        
        #TODO METHOD_1:

        # cafe={
        #     "id": random_cafe.id,
        #     "name": random_cafe.name,
        #     "map_url": random_cafe.map_url,
        #     "img_url": random_cafe.img_url,
        #     "location": random_cafe.location,
        #     "seats": random_cafe.seats,
        #     "has_toilet": random_cafe.has_toilet,
        #     "has_wifi": random_cafe.has_wifi,
        #     "has_sockets": random_cafe.has_sockets,
        #     "can_take_calls": random_cafe.can_take_calls,
        #     "coffee_price": random_cafe.coffee_price,
        # }
        # return jsonify(cafe)

        #TODO METHOD_2:
        return jsonify(random_cafe.to_dict())

@app.route("/all")
def get_all_data():
    result=db.session.execute(db.select(Cafe))
    cafes=result.scalars().all()
    cafes_dict={"cafes":[cafe.to_dict()  for cafe in cafes]}
    return jsonify(cafes_dict)
    #or return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

# from sqlalchemy import select
# stmt = select(user_table).where(user_table.c.name == "spongebob")
# print(stmt)


@app.route("/search")
def search_cafe():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    cafes = result.scalars().all()
    
    if cafes:
        cafes_dict = {"cafes": [cafe.to_dict() for cafe in cafes]}
        return jsonify(cafes_dict)
    else:
        return jsonify({"error": {"NotFound": "Sorry! We don't have a cafe at the location"}})


# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}),200


# HTTP PUT/PATCH - Update Record
@app.route("/update-price", methods=["PATCH"])
def update_price():
    cafe_id = request.args.get('cafe_id')
    new_price = request.args.get('price')  
    
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        ## Just add the code after the jsonify method. 200 = Ok
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        #404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

        

# HTTP DELETE - Delete Record
@app.route("/delete_cafe", methods=["DELETE"])
def delete_cafe():
    cafe_id=request.args.get("id")
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403



if __name__ == '__main__':
    app.run(debug=True)
