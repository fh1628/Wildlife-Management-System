from flask import Flask, request
import sqlite3
import json
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

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


@app.route('/add_location', methods=['POST'])
def add_location():
    data = request.json

    latitude = request.json["Latitude"]
    longitude = request.json['Longitude']
    name = data.get('LocationName', None)
    location_type = data.get('LocationType', None)
    elevation = data.get('Elevation', None)
    country = data.get('Country', None)
    area = data.get('Area', None)
    climate = data.get('Climate', None)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "INSERT INTO Location (Latitude, Longitude, LocationName, LocationType, Country, Area, Climate, Elevation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (latitude, longitude, name, location_type, country, area, climate, elevation)
    try:
        cursor.execute(query, values)
    
    except mysql.connector.IntegrityError as e:
        # Handle the IntegrityError
        error_msg = str(e)
        if (error_msg.startswith('1062')):
            error_msg = 'Duplicate'
        else:
            error_msg = 'Foreign'
        return jsonify({'error': error_msg}), 400
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': str(e)}), 500

    conn.commit()

    cursor.close()
    conn.close()
    return 'Location added'

@app.route('/update_location', methods=['PUT'])
def update_location():
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

    query = "Update Location SET LocationName=%s , LocationType=%s ,Country=%s ,Area=%s ,Climate=%s ,Elevation=%s WHERE Latitude=%s AND Longitude=%s"
    print(query)
    values = (name, location_type, country, area, climate, elevation, latitude, longitude)
    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Location updated'


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
    try:
        cursor.execute(query, values)
    
    except mysql.connector.IntegrityError as e:
        # Handle the IntegrityError
        error_msg = str(e)
        if (error_msg.startswith('1062')):
            error_msg = 'Duplicate'
        else:
            error_msg = 'Foreign'
        return jsonify({'error': error_msg}), 400
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': str(e)}), 500
    
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
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM LOCATION"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/get_habitats', methods=['GET'])
def get_habitats():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM HABITAT"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/get_populations', methods=['GET'])
def get_populations():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM POPULATION"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/get_species', methods=['GET'])
def get_species():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM SPECIES"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/get_researchers', methods=['GET'])
def get_researchers():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM RESEARCHER"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)


@app.route('/get_assistant_researchers', methods=['GET'])
def get_assistant_researchers():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM AssistantResearcher"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/get_conservation_organization', methods=['GET'])
def get_conservation_organization():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    query = "SELECT * FROM ConservationOrganization"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)


@app.route('/del_location', methods=['DELETE'])
def del_location():


    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    latitude = request.json["latitude"]
    longitude = request.json['longitude']

    cursor = conn.cursor()
    query = "DELETE FROM LOCATION WHERE  Latitude= %s AND Longitude = %s"
    val = (latitude, longitude)
    cursor.execute(query, val)
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Location Deleted'


@app.route('/del_habitat', methods=['DELETE'])
def del_habitat():


    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    
    name = request.json["habitat_name"]

    cursor = conn.cursor()
    query = "DELETE FROM Habitat WHERE HabitatName = %s"
    cursor.execute(query,(name,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Habitat Deleted'

@app.route('/del_species', methods=['DELETE'])
def del_species():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    scientific_name = request.json["scientific_name"]

    cursor = conn.cursor()
    query = "DELETE FROM Species WHERE  ScientificName = %s"
    cursor.execute(query, (scientific_name,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Species Deleted'

@app.route('/del_population', methods=['DELETE'])
def del_population():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    id = request.json["population_id"]

    cursor = conn.cursor()
    query = "DELETE FROM Population WHERE  PopulationID = %s"
    cursor.execute(query, (id,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Population Deleted'


@app.route('/del_researcher', methods=['DELETE'])
def del_researcher():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    email = request.json["reseracher_email"]

    cursor = conn.cursor()
    query = "DELETE FROM Researcher WHERE Email = %s"
    cursor.execute(query, (email,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Researcher Deleted'

@app.route('/del_assistant_researcher', methods=['DELETE'])
def del_assistant_researcher():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    assistant_email = request.json["assistant_email"]
    researcher_email = request.json["researcher_email"]

    cursor = conn.cursor()
    query = "DELETE FROM AssistantResearcher WHERE Email = %s AND ResearcherEmail = %s"
    cursor.execute(query, (assistant_email,researcher_email,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Assistant Researcher Deleted'


@app.route('/del_conservation_org', methods=['DELETE'])
def del_conservation_org():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    email = request.json["organization_email"]

    cursor = conn.cursor()
    query = "DELETE FROM ConservationOrganization WHERE ContactEmail = %s"
    cursor.execute(query, (email,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Organization Deleted'


@app.route('/del_organisation_protects', methods=['DELETE'])
def del_organisation_protects():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    email = request.json["organization_email"]
    population = request.json["population_id"]

    cursor = conn.cursor()
    query = "DELETE FROM Protects WHERE ContactEmail = %s AND PopulationID = %s"
    cursor.execute(query, (email,population,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Organization protects population Deleted'


@app.route('/del_habitat_threat', methods=['DELETE'])
def del_habitat_threat():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    habitat_name = request.json["habitat_name"]
    threat = request.json["threat"]

    cursor = conn.cursor()
    query = "DELETE FROM HThreats WHERE HabitatName = %s AND Threat = %s"
    cursor.execute(query, (habitat_name,threat,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Habitat Threat Deleted'

@app.route('/del_species_threat', methods=['DELETE'])
def del_species_threat():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    species_name = request.json["species_name"]
    threat = request.json["threat"]

    cursor = conn.cursor()
    query = "DELETE FROM SThreats WHERE ScientificName = %s AND Threat = %s"
    cursor.execute(query, (species_name,threat,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Species Threat Deleted'


@app.route('/del_researcher_project', methods=['DELETE'])
def del_researcher_project():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    email = request.json["researcher_email"]
    project = request.json["project"]

    cursor = conn.cursor()
    query = "DELETE FROM RProjects WHERE Email = %s AND Project = %s"
    cursor.execute(query, (email,project,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Researcher Project Deleted'


@app.route('/del_researcher_interest', methods=['DELETE'])
def del_researcher_interest():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    email = request.json["researcher_email"]
    interest = request.json["research_interest"]

    cursor = conn.cursor()
    query = "DELETE FROM RInterests WHERE Email = %s AND ResearchInterests = %s"
    cursor.execute(query, (email,interest,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Researcher Interest Deleted'

@app.route('/del_university_researcher', methods=['DELETE'])
def del_university_researcher():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    email = request.json["researcher_email"]

    cursor = conn.cursor()
    query = "DELETE FROM UniversityResearcher WHERE Email = %s"
    cursor.execute(query, (email,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'University Researcher Deleted'


@app.route('/del_company_researcher', methods=['DELETE'])
def del_company_researcher():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    email = request.json["researcher_email"]

    cursor = conn.cursor()
    query = "DELETE FROM CompanyResearcher WHERE Email = %s"
    cursor.execute(query, (email,))
    
    conn.commit()

    cursor.close()
    conn.close()
    return 'Company Researcher Deleted'


@app.route('/update_habitat', methods=['PUT'])
def update_habitat():
    data = request.json

    name = request.json["habitat_name"]
    degradation_level = data.get('degradation_level', None)
    conservation_status = data.get('conservation_status', None)
    habitat_type = data.get('type', None)
    latitude = data.get('latitude')
    longitude = data.get('longitude')


    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update Habitat SET HabitatType='%s' ,ConservationStatus='%s' ,DegradationLevel='%s' ,Latitude=%f ,Longitude=%f WHERE HabitatName='%s'" %(habitat_type, conservation_status, degradation_level, latitude, longitude, name)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Habitat updated'



@app.route('/update_population', methods=['PUT'])
def update_population():
    data = request.json

    population_id = request.json["population_id"]
    size = data.get('size', None)
    trend = data.get('trend', None)
    growth_rate = data.get('growth_rate', None)
    density = data.get('density')
    habitat_name = data.get('habitat_name')
    species_name = data.get('species_name')


    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update Population SET Size = %s, Trend = '%s', GrowthRate = %s, Density = %s, HabitatName ='%s', SpeciesScientificName ='%s' WHERE PopulationID = %s" %(size, trend, growth_rate, density, habitat_name, species_name, population_id)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Population updated'


@app.route('/update_species', methods=['PUT'])
def update_species():
    data = request.json

    scientific_name = request.json["scientific_name"]
    common_name = data.get('common_name', None)
    conservation_status = data.get('conservation_status', None)
    geographic_distribution = data.get('geographic_distribution', None)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update Species SET CommonName = '%s', ConservationStatus = '%s', GeographicDistribution = '%s' WHERE ScientificName = '%s'" %(common_name, conservation_status, geographic_distribution, scientific_name)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Researcher updated'


@app.route('/update_researcher', methods=['PUT'])
def update_researcher():
    data = request.json

    email = request.json["email"]
    name = data.get('name', None)
    phone = data.get('phone', None)
    expertise = data.get('expertise', None)
    species_name = data.get('species_name',None)
    population_id = data.get('population_id',None)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update Researcher SET Name = '%s', Phone = '%s', Expertise = '%s', SpeciesScientificName = '%s', PopulationID = %s WHERE Email = '%s'" %(name, phone, expertise, species_name, population_id, email)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Researcher updated'


@app.route('/update_conservation_org', methods=['PUT'])
def update_conservation_org():
    data = request.json

    email = request.json["contact_email"]
    name = data.get('name', None)
    mission = data.get('mission', None)
    website = data.get('website', None)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update ConservationOrganization SET Name = '%s', Mission = '%s', Website = '%s' WHERE ContactEmail = '%s'" %(name, mission, website, email)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Conservation organization updated'


@app.route('/update_assistant_researcher', methods=['PUT'])
def update_assistant_researcher():
    data = request.json

    email = request.json["assistant_email"]
    researcher_email = request.json["researcher_email"]
    name = data.get('name', None)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update AssistantResearcher SET Name = '%s' WHERE Email = '%s' AND ResearcherEmail = '%s'" %(name, email, researcher_email)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Assistant Researcher updated'


@app.route('/update_university_researcher', methods=['PUT'])
def update_university_researcher():
    data = request.json

    email = request.json["researcher_email"]
    name = data.get('name', None)
    university_name = data.get('university_name', None)
    tenure = data.get('tenure', None)
    

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update UniversityResearcher SET Name = '%s', UniversityName = '%s', Tenure = '%s' WHERE Email = '%s'" %(name, university_name, tenure, email)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'University Researcher updated'



@app.route('/update_company_researcher', methods=['PUT'])
def update_company_researcher():
    data = request.json

    email = request.json["researcher_email"]
    name = data.get('name', None)
    company_name = data.get('company_name', None)
    job_title = data.get('job_title', None)
    

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   

    cursor = conn.cursor()

    query = "Update CompanyResearcher SET Name = '%s', CompanyName = '%s', JobTitle = '%s' WHERE Email = '%s'" %(name, company_name, job_title, email)
    print(query)
    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
    return 'Company Researcher updated'

@app.route('/get_locations_filtered', methods=['GET'])
def get_locations_filtered():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    data = request.args

    print('data',data)
    print(data.items())

    query = "SELECT * FROM LOCATION WHERE "
    conditions = []
    for column, value in data.items():
        conditions.append(f"{column} = '{value}'")
    query += " AND ".join(conditions)
    print(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)


@app.route('/get_populations_filtered', methods=['GET'])
def get_populations_filtered():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="youss123",
        database="WILDLIFE_SCHEMA"
    )   
    cursor = conn.cursor()
    data = request.json

    query = "SELECT * FROM Population WHERE "
    conditions = []
    for column, value in data.items():
        conditions.append(f"{column} = '{value}'")
    query += " AND ".join(conditions)
    print(query)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)
