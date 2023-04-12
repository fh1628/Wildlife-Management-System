-- Query 1: Given a location name, list the name of all species in that location

-- Location: Tokyo

-- DELIMITER //

-- CREATE PROCEDURE get_species_in_location(IN location_name VARCHAR(255))
-- BEGIN
-- 	SELECT Species.ScientificName as 'Scientific Name', Species.CommonName as 'Common Name'
--     FROM Species
--     JOIN Population ON Species.ScientificName = Population.SpeciesScientificName
--     WHERE Population.HabitatName 
--     IN (SELECT HabitatName 
-- 		  FROM HABITAT_LOCATION_DETAILS
-- 		  WHERE LocationName=location_name);
-- END //

-- DELIMITER ;

-- CALL get_species_in_location('Tokyo'); 

-- Query 2: List all habitats occupied by a given species name (input is the Species Common Name)

-- DELIMITER //

-- CREATE PROCEDURE get_habitats_of_species(IN species_common_name VARCHAR(255))
-- BEGIN
-- SELECT PopulationHabitat.HabitatName as 'Habitat Name', 
-- 	   PopulationHabitat.HabitatType as 'Habitat Type',
-- 	   PopulationHabitat.DegradationLevel as 'Degradation Level', 
--     PopulationHabitat.ConservationStatus as 'Conservation Status'
-- FROM POPULATION_HABITAT_DETAILS PopulationHabitat
-- JOIN POPULATION_SPECIES_DETAILS PopulationSpecies ON PopulationHabitat.SpeciesScientificName = PopulationSpecies.SpeciesScientificName
-- WHERE PopulationSpecies.CommonName=species_common_name;
-- END //

-- DELIMITER ;

-- CALL get_habitats_of_species('Giant Panda');




-- Query 3:
-- DELIMITER //
-- CREATE PROCEDURE get_population_of_species(IN species_name VARCHAR(255))
-- BEGIN
-- SELECT Population.PopulationID as 'Population ID', Population.Size as 'Size'
--    FROM Population
--   WHERE Population.SpeciesScientificName = species_name;
-- END //
-- DELIMITER ;

-- CALL get_population_of_species('Panthera tigris');


-- Query 4: List all researchers studying a specific species or population
-- DELIMITER //
-- CREATE PROCEDURE get_researchers_of_species(IN species_name VARCHAR(255))
-- BEGIN
-- 	SELECT Researcher.Email as 'Email', Researcher.Name as 'Name', Researcher.Phone as 'Phone Number'
--   FROM Researcher
--   WHERE Researcher.SpeciesScientificName = species_name;
-- END //
-- DELIMITER ;

-- CALL get_researchers_of_species('Panthera tigris');


