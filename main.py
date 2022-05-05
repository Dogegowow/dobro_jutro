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

@app.route("/motor1")
def run_motor():
  print("Motor 1 pognan")

  #motor1
  DIR = 16   # Direction GPIO Pin
  STEP = 20  # Step GPIO Pin
  MOS = 23
  #settings
  CW = 1     # Clockwise Rotation
  CCW = 0    # Counterclockwise Rotation
  SPR = 200   # Steps per Revolution (360 / 7.5)

  motor.setup(STEP, DIR, MOS)
  motor.run(STEP, DIR, CCW, MOS, 1)
  return redirect(url_for("home"))

@app.route("/motor2")
def run_motor():
  print("Motor 2 pognan")
  
  #motor2
  DIR2 = 5
  STEP2 = 6
  MOS2 = 25
  #settings
  CW = 1     # Clockwise Rotation
  CCW = 0    # Counterclockwise Rotation
  SPR = 200   # Steps per Revolution (360 / 7.5)

  motor.setup(STEP2, DIR2, MOS2)
  motor.run(STEP2, DIR2, CCW, MOS2, 1)
  return redirect(url_for("home"))

@app.route("/motor3")
def run_motor():
  print("Motor 3 pognan")

  #motor3
  DIR3 = 26 
  STEP3 = 19
  MOS3 = 24
  #settings
  CW = 1     # Clockwise Rotation
  CCW = 0    # Counterclockwise Rotation
  SPR = 200   # Steps per Revolution (360 / 7.5)

  motor.setup(STEP3, DIR3, MOS3)
  motor.run(STEP3, DIR3, CCW, MOS3, 1)
  return redirect(url_for("home"))

app.run(host='0.0.0.0', port=8080)