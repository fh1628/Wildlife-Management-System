from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the application to use MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/Testing_DB'

# Create a SQLAlchemy object to interact with the database
db = SQLAlchemy(app)


# Define the Location model class
class Location(db.Model):
    __tablename__ = 'Location'
    Latitude = db.Column(db.Float, primary_key=True)
    Longitude = db.Column(db.Float, primary_key=True)
    LocationName = db.Column(db.String(255))
    LocationType = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    Area = db.Column(db.Float)
    Climate = db.Column(db.String(50))
    Elevation = db.Column(db.Float)

# Define the Habitat model class
class Habitat(db.Model):
    __tablename__ = 'Habitat'
    HabitatName = db.Column(db.String(255), primary_key=True)
    HabitatType = db.Column(db.String(50))
    ConservationStatus = db.Column(db.String(50))
    DegradationLevel = db.Column(db.String(50))
    Latitude = db.Column(db.Float, db.ForeignKey('Location.Latitude'), nullable=True)
    Longitude = db.Column(db.Float, db.ForeignKey('Location.Longitude'), nullable=True)
    Location = db.relationship(Location, backref='habitats')

# Define the HThreats model class
class HThreats(db.Model):
    __tablename__ = 'HThreats'
    HabitatName = db.Column(db.String(255), db.ForeignKey('Habitat.HabitatName'), primary_key=True)
    Threat = db.Column(db.String(255), primary_key=True)


with app.app_context():
    # Create the database tables (if they don't exist)
    db.create_all()
