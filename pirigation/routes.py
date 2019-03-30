from flask import Flask, render_template, url_for, flash, redirect, request 
from pirigation.models import Settings
from pirigation import app, db
from datetime import time
import pirigation.relays as relays

#comment
@app.route("/")
@app.route("/index")
def home():
    watersettings = Settings.query.all()
    return render_template('index.html', watersettings=watersettings, title="Home")

@app.route("/manual", methods=['GET', 'POST'])
def manual():
    if request.method == 'POST':
        if request.form.get('Master_ON') == 'ON':
            print("Master Valve On")
        if request.form.get('station_one_on') == 'ON':
            print("station 1 on")
            relays.z1_on()
        if request.form.get('station_two_on') == 'ON':
            print("station 2 on")
            relays.z2_on()
        if request.form.get('station_three_on') == 'ON':
            print("station 3 on")
            relays.z3_on()
        if request.form.get('station_four_on') == 'ON':
            print("station 4 on")
            relays.z4_on()
        if request.form.get('station_five_on') == 'ON':
            print("station 5 on")
            relays.z5_on()
        if request.form.get('station_six_on') == 'ON':
            print("Station 6 On")
            relays.z6_on()
        if request.form.get('station_seven_on') == 'ON':
            print("Station 7 On")
            relays.z7_on()
 
        elif request.form.get('Master_OFF') == 'OFF':
            print('Master Valve Off')
        elif request.form.get('station_one_off') == 'OFF':
            print("Station 1 Off")
            relays.z1_off()
        elif request.form.get('station_two_off') == 'OFF':
            print("Station 2 Off")
            relays.z2_off()
        elif request.form.get('station_three_off') == 'OFF':
            print("Station 3 Off")
            relays.z3_off()
        elif request.form.get('station_four_off') == 'OFF':
            print("Station 4 Off")
            relays.z4_off()
        elif request.form.get('station_five_off') == 'OFF':
            print("Station 5 Off")
            relays.z5_off()
        elif request.form.get('station_six_off') == 'OFF':
            print("Station 6 Off")
            relays.z6_off()
        elif request.form.get('station_seven_off') == 'OFF':
            print("Station 7 Off")
            relays.z7_off()

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
