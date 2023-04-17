from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the application to use MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/WILDLIFE_FLASK_SCHEMA'

# Create a SQLAlchemy object to interact with the database
db = SQLAlchemy(app)

# Define the Location model class
class Location(db.Model):
    __tablename__ = 'Location'
    Latitude = db.Column(db.Float, primary_key=True)
    Longitude = db.Column(db.Float, primary_key=True, index=True)
    LocationName = db.Column(db.String(255))
    LocationType = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    Area = db.Column(db.Float)
    Climate = db.Column(db.String(50))
    Elevation = db.Column(db.Float, index=True)

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

# Define the Habitat Threats model class
class HThreats(db.Model):
    __tablename__ = 'HThreats'
    HabitatName = db.Column(db.String(255), db.ForeignKey('Habitat.HabitatName'), primary_key=True)
    Threat = db.Column(db.String(255), primary_key=True)


# Define the Species model class
class Species(db.Model):
    __tablename__ = 'Species'
    ScientificName = db.Column(db.String(255), primary_key=True, index=True)
    CommonName = db.Column(db.String(255))
    ConservationStatus = db.Column(db.String(50))
    GeographicDistribution = db.Column(db.String(255))


# Define the Species Threats model class
class SThreats(db.Model):
    __tablename__ = 'SThreats'
    ScientificName = db.Column(db.String(255), db.ForeignKey('Species.ScientificName', ondelete='CASCADE'), primary_key=True)
    Threat = db.Column(db.String(255), primary_key=True)


# Define the Population model class
class Population(db.Model):
    __tablename__ = 'Population'
    PopulationID = db.Column(db.Integer, primary_key=True)
    Size = db.Column(db.Integer)
    Trend = db.Column(db.String(50))
    GrowthRate = db.Column(db.DECIMAL(5, 2))
    Density = db.Column(db.DECIMAL(10, 2))
    HabitatName = db.Column(db.String(255), db.ForeignKey('Habitat.HabitatName', ondelete='CASCADE'), index=True)
    SpeciesScientificName = db.Column(db.String(255), db.ForeignKey('Species.ScientificName', ondelete='CASCADE'))


# Define the Researcher model class
class Researcher(db.Model):
    __tablename__ = 'Researcher'
    Name = db.Column(db.String(255))
    Email = db.Column(db.String(255), primary_key=True)
    Phone = db.Column(db.String(255))
    Expertise = db.Column(db.String(255))
    SpeciesScientificName = db.Column(db.String(255), index=True)
    PopulationID = db.Column(db.Integer, db.ForeignKey('Population.PopulationID', ondelete='SET NULL'))

# Define the Assistant Researcher model class. It's a weak entity of Researcher
class AssistantResearcher(db.Model):
    __tablename__ = 'AssistantResearcher'
    Name = db.Column(db.String(255))
    Email = db.Column(db.String(255), primary_key=True)
    ResearcherEmail = db.Column(db.String(255), db.ForeignKey('Researcher.Email', ondelete='CASCADE'))
    researcher = db.relationship('Researcher', backref=db.backref('assistant_researchers', lazy=True))

# Define the Research Projects model class
class RProjects(db.Model):
    __tablename__ = 'RProjects'
    Email = db.Column(db.String(255), db.ForeignKey('Researcher.Email', ondelete='CASCADE'), primary_key=True)
    Project = db.Column(db.String(255))

# Define the Research Interests model class
class RInterests(db.Model):
    __tablename__ = 'RInterests'
    Email = db.Column(db.String(255), db.ForeignKey('Researcher.Email', ondelete='CASCADE'), primary_key=True)
    ResearchInterests = db.Column(db.String(50))

# Define the University Researcher model class
class UniversityResearcher(db.Model):
    __tablename__ = 'UniversityResearcher'
    Name = db.Column(db.String(255))
    UniversityName = db.Column(db.String(255))
    Tenure = db.Column(db.String(255))
    Email = db.Column(db.String(255), db.ForeignKey('Researcher.Email', ondelete='CASCADE'), primary_key=True)

# Define the Company Researcher model class
class CompanyResearcher(db.Model):
    __tablename__ = 'CompanyResearcher'
    Name = db.Column(db.String(255))
    CompanyName = db.Column(db.String(255))
    JobTitle = db.Column(db.String(255))
    Email = db.Column(db.String(255), db.ForeignKey('Researcher.Email', ondelete='CASCADE'), primary_key=True)

with app.app_context():
    # Create the database tables (if they don't exist)
    db.create_all()
