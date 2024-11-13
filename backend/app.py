from flask import Flask, jsonify, request
from models import db, VAWTData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vawt_data.db'
db.init_app(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = VAWTData.query.all()
    return jsonify([d.to_dict() for d in data])

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.get_json()
    vawt_data = VAWTData(wind_speed=new_data['wind_speed'], energy_output=new_data['energy_output'])
    db.session.add(vawt_data)
    db.session.commit()
    return jsonify(vawt_data.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
