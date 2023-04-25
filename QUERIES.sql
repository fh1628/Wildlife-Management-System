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

