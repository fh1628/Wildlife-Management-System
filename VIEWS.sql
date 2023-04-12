-- CREATE VIEW HABITAT_LOCATION_DETAILS AS
-- SELECT Habitat.HabitatName, Location.LocationName
-- FROM Habitat
-- JOIN Location ON Habitat.Longitude = Location.Longitude AND Habitat.Latitude = Location.Latitude;

CREATE VIEW POPULATION_HABITAT_DETAILS AS
SELECT Population.SpeciesScientificName, Habitat.*
FROM Population JOIN Habitat ON Population.HabitatName = Habitat.HabitatName;

CREATE VIEW POPULATION_SPECIES_DETAILS AS
SELECT *
FROM Population JOIN Species ON Population.SpeciesScientificName = Species.ScientificName;