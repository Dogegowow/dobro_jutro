from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/motor")
def motor():
  print("Motor pognan")
  return redirect(url_for("home"))

app.run(host='0.0.0.0', port=8080)