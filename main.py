from flask import Flask, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"
class List(db.Model):
    id = db.Column(db.String, primary_key=True)
    url = db.Column(db.String)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
db.init_app(app)

@app.route("/")
def root():
    return send_from_directory("./client/dist", "index.html")

@app.route("/<path:path>")
def assets(path):
    return send_from_directory("./client/dist", path)

@app.route("/add_link", methods = ["GET", "POST"])
def add():
    link = request.get_json()
    print(link)
    new_link = List(url=link["url"], id=link["id"])
    db.session.add(new_link)
    db.session.commit()
    return request.get_json()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)