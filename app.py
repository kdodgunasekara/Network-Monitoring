from flask import Flask,render_template
from db import connect

app=Flask(__name__)

@app.route("/")

def home():

    db=connect()

    cur=db.cursor()

    cur.execute(

    "SELECT * FROM devices"

    )

    devices=cur.fetchall()

    return render_template(

        "index.html",

        devices=devices

    )

app.run(debug=True)