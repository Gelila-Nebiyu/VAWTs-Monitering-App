from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class VAWTData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wind_speed = db.Column(db.Float)
    energy_output = db.Column(db.Float)
    efficiency = db.Column(db.Float)

    def to_dict(self):
        return {'id': self.id, 'wind_speed': self.wind_speed, 'energy_output': self.energy_output, 'efficiency': self.efficiency}


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
