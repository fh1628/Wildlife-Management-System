from flask import Flask, request
import sqlite3
import json
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/execute_sql_file')
def execute_sql_file():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        # database="WILDLIFE_FLASK_SCHEMA"
    )   

    cursor = conn.cursor()

    with open('CREATE_TABLES.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    sql_statements = sql_script.split(';')

    for statement in sql_statements:
        if statement.strip() != '':
            cursor.execute(statement)

    conn.commit()

    cursor.close()
    conn.close()

    return 'SQL script executed successfully'

@app.route('/add_location', methods=['POST'])
def add_location():
    data = request.json

    latitude = request.json["latitude"]
    longitude = request.json['longitude']
    name = data.get('location_name', None)
    location_type = data.get('location_type', None)
    elevation = data.get('location_elevation', None)
    country = data.get('location_country', None)
    area = data.get('location_area', None)
    climate = data.get('location_climate', None)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "INSERT INTO Location (Latitude, Longitude, LocationName, LocationType, Country, Area, Climate, Elevation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (latitude, longitude, name, location_type, country, area, climate, elevation)
    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Data added'

@app.route('/add_habitat', methods=['POST'])
def add_habitat():
    data = request.json

    name = request.json["habitat_name"]
    degradation_level = data.get('degradation_level', None)
    conservation_status = data.get('conservation_status', None)
    habitat_type = data.get('type', None)
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    threats = data.get('threats')
    all_threats = threats.split(", ")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "INSERT INTO Habitat (HabitatName, HabitatType, ConservationStatus, DegradationLevel, Latitude, Longitude) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, habitat_type, conservation_status, degradation_level, latitude, longitude)
    cursor.execute(query, values)

    for i in range(len(all_threats)):
        query = "INSERT INTO HThreats (HabitatName, Threat) VALUES ('{}', '{}')".format(name, all_threats[i])
        cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Data added'


@app.route('/add_species', methods=['POST'])
def add_species():
    data = request.json

    scientific_name = data.get('scientific_name')
    common_name = data.get('common_name', None)
    conservation_status = data.get('conservation_status', None)
    geographic_distribution = data.get('geographic_distribution', None)
    threats = data.get('threats')
    all_threats = threats.split(", ")
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()


    query = "INSERT INTO Species (ScientificName, CommonName, ConservationStatus, GeographicDistribution) VALUES (%s, %s, %s, %s)"
    values = (scientific_name, common_name, conservation_status, geographic_distribution)
    cursor.execute(query, values)


    for i in range(len(all_threats)):
        query = "INSERT INTO SThreats (ScientificName, Threat) VALUES ('{}', '{}')".format(scientific_name, all_threats[i])
        cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Data added'


@app.route('/add_population', methods=['POST'])
def add_population():
    data = request.json

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    population_id = data.get('population_id')
    size = data.get('population_size', None)
    trend = data.get('population_trend', None)
    growth_rate = data.get('growth_rate', None)
    density = data.get('density', None)
    habitat_name = data.get('habitat_name')
    specifies_scientific_name = data.get('species_scientific_name')

    query = "INSERT INTO Population (PopulationID, Size, Trend, GrowthRate, Density, HabitatName, SpeciesScientificName) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (population_id, size, trend, growth_rate, density, habitat_name, specifies_scientific_name)
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return 'Data added'


