from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["form_example"]
collection = db["user_data"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        if name:
            user_data = {"name": name}
            collection.insert_one(user_data)
        else:
            return "Name cannot be empty!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
