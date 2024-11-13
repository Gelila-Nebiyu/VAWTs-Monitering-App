from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class VAWTData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wind_speed = db.Column(db.Float, nullable=False)
    energy_output = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'wind_speed': self.wind_speed, 'energy_output': self.energy_output}
