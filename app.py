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
    type = data.get('location_type', None)
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
    values = (latitude, longitude, name, type, country, area, climate, elevation)
    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    return 'data added'
