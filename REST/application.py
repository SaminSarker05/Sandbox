from flask import Flask, jsonify
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
# configures flask app instance to db instance

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# creates a new table and Model
# sqlalchemy provides ORM and mapping of Python classes to database tables

class Drink(db.Model):
  # table columns
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(120))


  def __repr__(self):
    return f"{self.name} - {self.description}"


@app.route("/")
def index():
  return "hello world"

@app.route('/drinks')
def get_drinks():
  drinks = {
    "cola": ['coke']
  }
  return jsonify(drinks), 200


if __name__ == "__main__":  
  app.run(debug = True)