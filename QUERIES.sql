-- Query 1: Given a location name, list the name of all species in that location

-- Location: Tokyo

DELIMITER //

CREATE PROCEDURE get_species_in_location(IN location_name VARCHAR(255))
BEGIN
	SELECT Species.ScientificName as 'Scientific Name', Species.CommonName as 'Common Name'
    FROM Species
    JOIN Population ON Species.ScientificName = Population.SpeciesScientificName
    WHERE Population.HabitatName 
    IN (SELECT HabitatName 
		  FROM HABITAT_LOCATION_DETAILS
		  WHERE LocationName=location_name);
END //

DELIMITER ;

CALL get_species_in_location('Tokyo');



-- Query 3:
DELIMITER //
CREATE PROCEDURE get_population_of_species(IN species_name VARCHAR(255))
BEGIN
	SELECT Population.PopulationID as 'Population ID', Population.Size as 'Size'
    FROM Population
    WHERE Population.SpeciesScientificName = species_name;
END //
DELIMITER ;

CALL get_population_of_species('Panthera tigris');



