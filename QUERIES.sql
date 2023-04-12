-- Query 1: Given a location name, list the name of all species in that location

-- Location: Tokyo

DELIMITER //

CREATE PROCEDURE GET_SPECIES_IN_LOCATION(IN location_name VARCHAR(255))
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

CALL GET_SPECIES_IN_LOCATION('Tokyo');

