from flask import Flask
from flask_restful import Resource, Api
from flask import request
from controllers import author
from controllers import quotes
from flask_sqlalchemy import SQLAlchemy
from flask_api import status
import json
from flask import jsonify

app = Flask(__name__)
#api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://antuan:secret@localhost/quotes_db"
db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def serialize(self):
       return {
           'id'         : self.id,
           'name': self.name
       }

@app.route("/")
def status():
    return { "status": "working"}

@app.route("/api/random")
def random_quote():
    return { "quote":"naosehusnoahunsoehsun"}

@app.route("/api/<author>/quote")
def quote_from_author(author):
    res = "quote from: " + author
    return { "quote": res }

@app.route("/api/authors", methods=["GET", "POST"])
def handle_authors():
    if request.method == "GET":
        #res = author.AuthorController.list()
        return jsonify(authors=[i.serialize for i in Author.query.all()])    
    else:
        #res = author.AuthorController.create("antuan")
        new_author = Author("antuan6")
        db.session.add(new_author)
        db.session.commit()
        print(new_author)
        response = json.dumps({ "data": new_author.serialize }) 
        return response

@app.route("/api/quote/<int:author_id>", methods=["POST"])
def create_quote(author_id):
    return {"data":"created"}

@app.route("/about")
def about():
    return { "data": "this is about" }

if __name__ == '__main__':
    app.run(debug=True)
