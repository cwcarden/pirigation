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

@app.route("/manual", methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        if request.form.get('mv_on') == 'Master':
            print("The Master is on")
            
        elif request.form.get('mv_off') == 'OFF':
            print("Master off")
        
        if request.form.get('z1_on') == 'Zone 1':
            print('zone 1 on')
        elif request.form.get('z1_off') == 'OFF':
            print('zone 1 off')

        if request.form.get('z2_on') == 'Zone 2':
            print('zone 2 on')
        elif request.form.get('z2_off') == 'OFF':
            print('zone 2 off')

        if request.form.get('z3_on') == 'Zone 3':
            print('zone 3 on')
        elif request.form.get('z3_off') == 'OFF':
            print('zone 3 off')

        if request.form.get('z4_on') == 'Zone 4':
            print('zone 4 on')
        elif request.form.get('z4_off') == 'OFF':
            print('zone 4 off')

        if request.form.get('z5_on') == 'Zone 5':
            print('zone 5 on')
        elif request.form.get('z5_off') == 'OFF':
            print('zone 5 off')

        if request.form.get('z6_on') == 'Zone 6':
            print('zone 6 on')
        elif request.form.get('z6_off') == 'OFF':
            print('zone 6 off')

        else:
            return render_template('manual.html', title='Manual Settings')
    elif request.method =='GET':
        print("No Post Back Call")
    return render_template('manual.html')

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