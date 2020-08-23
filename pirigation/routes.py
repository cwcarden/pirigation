from flask import Flask, render_template, url_for, flash, redirect, request, Response
import requests
from pirigation.models import Settings
from pirigation import app, db
from datetime import time
import io
import random 
#from pirigation.lib import scheduler

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html', title="Home", watering=True)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template('settings.html', settings=settings)
    elif request.method == 'GET':
        return render_template('settings.html')

@app.route('/post_data', methods=['POST'])
def post_data():
    usersett = Settings(
    request.form.get('s1_runtime'),
    request.form.get('s2_runtime'), request.form.get('s3_runtime'),
    request.form.get('s4_runtime'), request.form.get('s5_runtime'),
    request.form.get('s6_runtime'),request.form.get('watertime'), 
    request.form.get('monday'), request.form.get('tuesday'), 
    request.form.get('wednesday'), request.form.get('thursday'),
    request.form.get('friday'), request.form.get('saturday'),
    request.form.get('sunday')) 
 
    db.session.add(usersett)
    db.session.commit()
    return redirect(url_for('settings'))

@app.route('/water', methods=['GET'])
def water():
    return render_template("water.html")

@app.route('/weather', methods=['GET'])
def weather():
    return render_template("weather.html")

start_time = {
        "mv": " - Initializing",
        "z1": " - Initializing",
        "z2": " - Initializing",
        "z3": " - Initializing",
        "z4": " - Initializing",
        "z5": " - Initializing",
        "z6": " - Initializing",
        "z7": " - Initializing",
        }

status = {
    "mv": "Inactive",
    "z1": "Inactive",
    "z2": "Inactive",
    "z3": "Inactive",
    "z4": "Inactive",
    "z5": "Inactive",
    "z6": "Inactive",
    "z7": "Inactive",
}

@app.route("/manual", methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        if request.form.get('mv_on') == 'ON':
            status.update(mv = "Active")
            relays.mv_on()
            start_time.update(mv = time.ctime())
            
        elif request.form.get('mv_off') == 'OFF':
            status.update(mv = "Inactive")
            relays.mv_off()
            start_time.update(mv = "")

        if request.form.get('z1_on') == 'ON':
            status.update(z1 = "Active")
            relays.one_on()
            start_time.update(z1 = time.ctime())

        elif request.form.get('z1_off') == 'OFF':
            status.update(z1 = "Inactive")
            relays.one_off()
            start_time.update(z1 = "")
            
        if request.form.get('z2_on') == 'ON':
            status.update(z2 = "Active")
            relays.two_on()
            start_time.update(z2 = time.ctime())
            
        elif request.form.get('z2_off') == 'OFF':
            status.update(z2 = "Inactive")
            relays.two_off()
            start_time.update(z2 = "")
           
        if request.form.get('z3_on') == 'ON':
            status.update(z3 = "Active")
            relays.three_on()
            start_time.update(z3 = time.ctime())
            
        elif request.form.get('z3_off') == 'OFF':
            status.update(z3 = "Inactive")
            relays.three_off()
            start_time.update(z3 = "")
            
        if request.form.get('z4_on') == 'ON':
            status.update(z4 = "Active")
            relays.four_on()
            start_time.update(z4 = time.ctime())
            
        elif request.form.get('z4_off') == 'OFF':
             status.update(z4 = "Inactive")
             relays.four_off()
             start_time.update(z4 = "")
           
        if request.form.get('z5_on') == 'ON':
            status.update(z5 = "Active")
            relays.five_on()
            start_time.update(z5 = time.ctime())
            
        elif request.form.get('z5_off') == 'OFF':
            status.update(z5 = "Inactive")
            relays.five_off()
            start_time.update(z5 = "")
            
        if request.form.get('z6_on') == 'ON':
            status.update(z6 = "Active")
            relays.six_on()
            start_time.update(z6 = time.ctime())
            
        elif request.form.get('z6_off') == 'OFF':
            status.update(z6 = "Inactive")
            relays.six_off()
            start_time.update(z6 = "")
            
        if request.form.get('z7_on') == 'ON':
            status.update(z7 = "Active")
            relays.seven_on()
            start_time.update(z7 = time.ctime())
            
        elif request.form.get('z7_off') == 'OFF':
            status.update(z7 = "Inactive")
            relays.seven_off()
            start_time.update(z7 = "")
            

        else:
            return render_template('index.html', title='PIrigation Control', status=status, start_time=start_time)
    elif request.method =='GET':
        print("No Post Back Call")
    return render_template('manual.html', status=status, start_time=start_time)