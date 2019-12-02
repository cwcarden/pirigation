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
    return render_template('index.html', title="Home", watering=False)

@app.route("/manual", methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        if request.form.get('mv_on') == 'ON':
            requests.post('http://192.168.1.32:4000/relays_on', data={'relay':'mv_on'})
            
        elif request.form.get('mv_off') == 'OFF':
            requests.post('http://192.168.1.32:4000/relays_on', data={'relay':'mv_on'})
        
        if request.form.get('z1_on') == 'ON':
            relays.z1_on()
        elif request.form.get('z1_off') == 'OFF':
            print('zone 1 off')

        if request.form.get('z2_on') == 'ON':
            relays.z2_on()
        elif request.form.get('z2_off') == 'OFF':
            print('zone 2 off')

        if request.form.get('z3_on') == 'ON':
            relays.z3_on()
        elif request.form.get('z3_off') == 'OFF':
            print('zone 3 off')

        if request.form.get('z4_on') == 'ON':
            relays.z4_on()
        elif request.form.get('z4_off') == 'OFF':
            print('zone 4 off')

        if request.form.get('z5_on') == 'ON':
            relays.z5_on()
        elif request.form.get('z5_off') == 'OFF':
            print('zone 5 off')

        if request.form.get('z6_on') == 'ON':
            relays.z6_on()
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
    request.form.get('enabled_a'), request.form.get('s1_runtime'),
    request.form.get('s2_runtime'), request.form.get('s3_runtime'),
    request.form.get('s4_runtime'), request.form.get('s5_runtime'),
    request.form.get('s6_runtime'), request.form.get('s7_runtime'),
    request.form.get('watertime'), request.form.get('monday'),
    request.form.get('tuesday'), request.form.get('wednesday'),
    request.form.get('thursday'),request.form.get('friday'),
    request.form.get('saturday'),request.form.get('sunday')) 
    db.session.add(usersett)
    db.session.commit()
    return redirect(url_for('settings'))
