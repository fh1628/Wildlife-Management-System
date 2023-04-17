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

