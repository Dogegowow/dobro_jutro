from flask import Flask, render_template, request, redirect, url_for
import random
from time import sleep
import RPi.GPIO as GPIO
import motor
import test

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("app.html")

@app.route("/motor/<id1>/<obrati1>/<id2>/<obrati2>/<id3>/<obrati3>")
def run_motor(id1, obrati1, id2, obrati2, id3, obrati3):
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
  motor.setup(motors[int(id1)]["step"], motors[int(id1)]["dir"], motors[int(id1)]["mos"])
  motor.run(motors[int(id1)]["step"], motors[int(id1)]["dir"], CCW, motors[int(id1)]["mos"], float(obrati1))
  
  motor.setup(motors[int(id2)]["step"], motors[int(id2)]["dir"], motors[int(id2)]["mos"])
  motor.run(motors[int(id2)]["step"], motors[int(id2)]["dir"], CCW, motors[int(id2)]["mos"], float(obrati2)) 
  
  motor.setup(motors[int(id3)]["step"], motors[int(id3)]["dir"], motors[int(id3)]["mos"])
  motor.run(motors[int(id3)]["step"], motors[int(id3)]["dir"], CCW, motors[int(id3)]["mos"], float(obrati3))
  
  return redirect(url_for("home"))

app.run(host='0.0.0.0', port=8080)