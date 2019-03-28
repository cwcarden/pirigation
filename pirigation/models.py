from datetime import datetime
from pirigation import db
from flask_sqlalchemy import SQLAlchemy 

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
