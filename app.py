from flask import Flask
from flask_restful import Resource, Api
from flask import request
from controllers import author
from controllers import quotes

app = Flask(__name__)
api = Api(app)

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
        res = author.AuthorController.list()
        print(res)
        return { "authors":["list"] }
    else:
        res = author.AuthorController.create("antuan")
        print(res)
        return { "data": "author created" }

@app.route("/api/quote/<int:author_id>", methods=["POST"])
def create_quote(author_id):
    return {"data":"created"}

@app.route("/test")
def hello_world():
    return {'test': 'tset'}

@app.route("/about")
def about():
    return { "data": "this is about" }

if __name__ == '__main__':
    app.run(debug=True)
