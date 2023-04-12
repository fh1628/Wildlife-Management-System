CREATE VIEW HABITAT_LOCATION_DETAILS AS
SELECT Habitat.HabitatName, Location.LocationName
FROM Habitat
JOIN Location ON Habitat.Longitude = Location.Longitude AND Habitat.Latitude = Location.Latitude;