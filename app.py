from flask import Flask, jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/parkingdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class VehicleType(db.Model):
    __tablename__ = 'vehicle_type'
    type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    cost = db.Column(db.Integer)

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    vehicle_id = db.Column(db.String(10), primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('vehicle_type.type_id'))
    in_time = db.Column(db.DateTime)
    out_time = db.Column(db.DateTime)
    price = db.Column(db.Integer)

class ParkingSpace(db.Model):
    __tablename__ = 'parking_space'
    space_id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('vehicle_type.type_id'))
    vehicle_id = db.Column(db.String(10), db.ForeignKey('vehicle.vehicle_id'))

@app.route('/')
def parking_space():
    spaces = ParkingSpace.query.all()
    
    grid = [[None for _ in range(5)] for _ in range(5)]
    for space in spaces:
        grid[(space.space_id - 1) // 5][(space.space_id - 1) % 5] = 'X' if space.vehicle_id else None

    return render_template('parking.html', grid=grid)

if __name__ == '__main__':
    app.run(debug=True)