from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import db, VAWTData, User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vawt_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/api/data', methods=['GET'])
def get_data():
    data = VAWTData.query.all()
    return jsonify([d.to_dict() for d in data])


@app.route('/api/simulate', methods=['POST'])
def simulate_conditions():
    wind_speed = request.json.get('wind_speed', 0)
    energy_output = wind_speed * 1.5  # Dummy calculation
    return jsonify({'energy_output': energy_output})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Login failed!"})


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"})


if __name__ == '__main__':
    app.run(debug=True)
