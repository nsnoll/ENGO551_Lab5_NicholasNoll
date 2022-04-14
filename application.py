from flask import Flask, render_template, request
import requests
import datetime

app=Flask(__name__)


@app.route("/")
def start_mapping():
    return render_template("Lab5_Polygon_NN.html")


if __name__== "__main__" :
    app.run(debug=True)