from flask import Flask, render_template, request, redirect, url_for
import random
from time import sleep
import RPi.GPIO as GPIO
import motor
import test

app = Flask(__name__)

@app.route("/")
def home():
  print(dir(motor))
  return render_template("index.html")

@app.route("/motor/<id>")
def run_motor(id):
  print("Motor " + id + " pognan")
  motors = [
    {
      "dir": 16,
      "step": 20,
      "mos": 23
    },
    {
      "dir": 5,
      "step": 6,
      "mos": 25
    },
    {
      "dir": 26,
      "step": 19,
      "mos": 24
    }
    
  ]

  #settings
  CW = 1     # Clockwise Rotation
  CCW = 0    # Counterclockwise Rotation
  
  #for m in motors:
  motor.setup(motors[int(id)]["step"], motors[int(id)]["dir"], motors[int(id)]["mos"])

  #for m in motors:
  motor.run(motors[int(id)]["step"], motors[int(id)]["dir"], CCW, motors[int(id)]["mos"], 1)

  return redirect(url_for("home"))

app.run(host='0.0.0.0', port=8080)