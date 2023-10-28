from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        if name:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="form_example"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user_data (name) VALUES (%s)", (name,))
            conn.commit()
            conn.close()
        else:
            return "Name cannot be empty!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
