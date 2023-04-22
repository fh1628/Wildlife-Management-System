from flask import Flask, request
import sqlite3
import json
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/create_tables')
def create_tables():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
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

    return 'Tables created successfully'

@app.route('/create_views')
def create_views():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    with open('VIEWS.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    sql_statements = sql_script.split(';')

    for statement in sql_statements:
        if statement.strip() != '':
            cursor.execute(statement)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Views created successfully'

@app.route('/create_indices')
def create_indices():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    with open('INDICES.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    sql_statements = sql_script.split(';')

    for statement in sql_statements:
        if statement.strip() != '':
            cursor.execute(statement)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Indices created successfully'

@app.route('/create_prerequisites')
def create_prerequisites():
    create_tables()
    create_views()
    create_indices()
    return "Tables, views, and indices created successfully"


@app.route('/generate_sample_data')
def generate_sample_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    with open('GENERATE_SAMPLE_DATA.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    sql_statements = sql_script.split(';')

    for statement in sql_statements:
        if statement.strip() != '':
            cursor.execute(statement)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Sample data created successfully'


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
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "INSERT INTO Location (Latitude, Longitude, LocationName, LocationType, Country, Area, Climate, Elevation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (latitude, longitude, name, location_type, country, area, climate, elevation)
    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Location added'

@app.route('/generate_sample_data')
def generate_sample_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    with open('GENERATE_SAMPLE_DATA.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    sql_statements = sql_script.split(';')

    for statement in sql_statements:
        if statement.strip() != '':
            cursor.execute(statement)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Sample data created successfully'

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
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "INSERT INTO Habitat (HabitatName, HabitatType, ConservationStatus, DegradationLevel, Latitude, Longitude) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, habitat_type, conservation_status, degradation_level, latitude, longitude)
    cursor.execute(query, values)

    for i in range(len(all_threats)):
        query = "INSERT INTO HThreats (HabitatName, Threat) VALUES(%s, %s)"
        values = (name, all_threats[i])
        cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Habitat added'


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
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()


    query = "INSERT INTO Species (ScientificName, CommonName, ConservationStatus, GeographicDistribution) VALUES (%s, %s, %s, %s)"
    values = (scientific_name, common_name, conservation_status, geographic_distribution)
    cursor.execute(query, values)


    for i in range(len(all_threats)):
        query = "INSERT INTO SThreats (ScientificName, Threat) VALUES (%s, %s)"
        values = (scientific_name, all_threats[i])
        cursor.execute(query,values)

    conn.commit()

    cursor.close()
    conn.close()

    return 'Species added'


@app.route('/add_population', methods=['POST'])
def add_population():
    data = request.json

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
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
    return 'Population added'

@app.route('/add_researcher', methods=['POST'])
def add_researcher():
    data = request.json

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    name = data.get('name', None)
    email = data.get('email')
    phone = data.get('phone_number', None)
    expertise = data.get('expertise', None)
    specifies_scientific_name = data.get('species_scientific_name', None)
    population_id = data.get('population_id')

    
    query = "INSERT INTO Researcher (Name, Email, Phone, Expertise, SpeciesScientificName, PopulationID) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name, email, phone, expertise, specifies_scientific_name, population_id)
    cursor.execute(query, values)
    conn.commit()

    researcher_type = data.get('researcher_type')
    if researcher_type == 'University':
        university_name = data.get('university_name', None)
        tenure= data.get('tenure', None)
        query = "INSERT INTO UniversityResearcher (Name, UniversityName, Tenure, Email) VALUES (%s, %s, %s, %s)"
        values = (name, university_name, tenure, email)
        cursor.execute(query, values)
    elif researcher_type == 'Company':
        company_name = data.get('company_name', None)
        job_title = data.get('job_title', None)
        query = "INSERT INTO CompanyResearcher (Name, CompanyName, JobTitle, Email) VALUES (%s, %s, %s, %s)"
        values = (name, company_name, job_title, email)
        cursor.execute(query, values)

    cursor.close()
    conn.close()
    return researcher_type + ' Researcher added'


@app.route('/add_research_project', methods=['POST'])
def add_research_project():
    data = request.json

    email = data.get('email')
    projects = data.get('projects')
    all_projects = projects.split(", ")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()
    for i in range(len(all_projects)):
        query = "INSERT INTO RProjects (Email, Project) VALUES (%s, %s)"
        values = (email, all_projects[i])
        cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Research Projects added'

@app.route('/add_research_interest', methods=['POST'])
def add_research_interest():
    data = request.json

    email = data.get('email')
    interests = data.get('research_interest')
    all_interests = interests.split(", ")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    for i in range (len(all_interests)):
        query = "INSERT INTO RInterests (Email, ResearchInterests) VALUES (%s, %s)"
        values = (email, all_interests[i])
        cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Research Interests added'

@app.route('/add_conservation_organization', methods=['POST'])
def add_conservation_organization():
    data = request.json

    email = data.get('contact_email')
    name = data.get('name', None)
    mission = data.get('mission', None)
    website = data.get('website', None)
    population_ids = data.get('population_ids', None)
    all_population_ids = population_ids.split(", ")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "INSERT INTO ConservationOrganization (ContactEmail, Name, Mission, Website) VALUES (%s, %s, %s, %s)"
    values = email, name, mission, website
    cursor.execute(query, values)

    conn.commit()

    for i in range(len(all_population_ids)):
        query = "INSERT INTO Protects (ContactEmail, PopulationID) VALUES (%s, %s)"
        values = (email, all_population_ids[i])
        cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return 'Conservation Organization successfully added'


@app.route('/add_assistant_researcher', methods=['POST'])
def add_assistant_researcher():
    data = request.json

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    name = data.get('name', None)
    email = data.get('email')
    researcher_email = data.get('researcher_email')

    query = "INSERT INTO AssistantResearcher (Name, Email, ResearcherEmail) VALUES (%s, %s, %s)"
    values = (name, email, researcher_email)
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return 'Assistant Researcher added'

@app.route('/get_locations', methods=['GET'])
def get_locations():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM LOCATION"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)
