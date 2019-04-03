from datetime import datetime
from pirigation import db
from flask_sqlalchemy import SQLAlchemy 
import sqlite3

class Settings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    enabled_a = db.Column(db.String(5), nullable=True)
    s1_runtime = db.Column(db.Integer, nullable=True)
    s2_runtime = db.Column(db.Integer, nullable=True)
    s3_runtime = db.Column(db.Integer, nullable=True)
    s4_runtime = db.Column(db.Integer, nullable=True)
    s5_runtime = db.Column(db.Integer, nullable=True)
    s6_runtime = db.Column(db.Integer, nullable=True)
    s7_runtime = db.Column(db.Integer, nullable=True)
    watertime = db.Column(db.String(15), nullable=True)
    monday = db.Column(db.String(5), nullable=True)
    tuesday = db.Column(db.String(5), nullable=True)
    wednesday = db.Column(db.String(5), nullable=True)
    thursday = db.Column(db.String(5), nullable=True)
    friday = db.Column(db.String(5), nullable=True)
    saturday = db.Column(db.String(5), nullable=True)
    sunday = db.Column(db.String(5), nullable=True)

    def __init__(self, enabled_a, s1_runtime, s2_runtime, s3_runtime, s4_runtime, s5_runtime, s6_runtime, s7_runtime, watertime, monday, tuesday, wednesday, thursday, friday, saturday, sunday):

        self.enabled_a = enabled_a
        self.s1_runtime = s1_runtime
        self.s2_runtime = s2_runtime 
        self.s3_runtime = s3_runtime 
        self.s4_runtime = s4_runtime
        self.s5_runtime = s5_runtime
        self.s6_runtime = s6_runtime
        self.watertime = watertime
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
    
    def __repr__(self):
        return '<Station A %r>' % self.enabled_a
        return '<Station 1 %r>' % self.s1_runtime
def create_weather():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE weather (
        id INTEGER PRIMARY KEY,
        api_key TEXT NOT NULL, 
        longitude TEXT NOT NULL,
        lattitude TEXT NOT NULL); ''')

#creates default schedule table
def create_schedule():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE schedule (
        id INTEGER PRIMARY KEY,
        schedule_id INTEGER, 
        enabled INTEGER NOT NULL,
        start_time TEXT NOT NULL,
        sun_enabled INTEGER NOT NULL,
        mon_enabled INTEGER NOT NULL,
        tue_enabled INTEGER NOT NULL,
        wed_enabled INTEGER NOT NULL,
        thu_enabled INTEGER NOT NULL,
        fri_enabled INTEGER NOT NULL,
        sat_enabled INTEGER NOT NULL); ''')

#creates default zone table
def create_zone():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE zone (
        id integer primary key,
        zone_id INTEGER NOT NULL,
        zone_enabled INTEGER NOT NULL,
        runtime INTEGER NOT NULL,
        schedule_id INTEGER NOT NULL,
        FOREIGN KEY(schedule_id) REFERENCES schedule(schedule_id));''')