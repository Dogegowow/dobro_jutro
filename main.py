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
  #test.a()
  return render_template("index.html")

@app.route("/motor")
def motor():
  print("Motor pognan")
  DIR = 20   # Direction GPIO Pin
  STEP = 21  # Step GPIO Pin
  MOS = 23
  #motor2
  DIR2 = 5
  STEP2 = 6
  MOS2 = 24
  #settings
  CW = 1     # Clockwise Rotation
  CCW = 0    # Counterclockwise Rotation
  SPR = 200   # Steps per Revolution (360 / 7.5)
  motor.setup()
  motor.run(STEP, DIR, CCW, MOS, 2)
  return redirect(url_for("home"))

app.run(host='0.0.0.0', port=8080)