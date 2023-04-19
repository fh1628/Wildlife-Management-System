from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

def get_species_in_location(location_name):
    query = text("""
        SELECT Species.ScientificName as 'Scientific Name', Species.CommonName as 'Common Name'
        FROM Species
        JOIN Population ON Species.ScientificName = Population.SpeciesScientificName
        WHERE Population.HabitatName 
        IN (SELECT HabitatName 
            FROM HABITAT_LOCATION_DETAILS
            WHERE LocationName=:location_name)
    """)
    result = db.engine.execute(query, location_name=location_name)
    return result.fetchall()