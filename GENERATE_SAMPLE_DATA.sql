-- Location
INSERT INTO Location (Latitude, Longitude, LocationName, LocationType, Area, Climate, Elevation)
VALUES
    (40.7128, -74.0060, 'New York City', 'City', 468.9, 'Humid Subtropical', 10),
    (51.5074, -0.1278, 'London', 'City', 1572, 'Temperate Maritime', 35),
    (35.6895, 139.6917, 'Tokyo', 'City', 2187, 'Humid Subtropical', 131),
    (19.4326, -99.1332, 'Mexico City', 'City', 1485, 'Humid Subtropical', 2240),
    (48.8566, 2.3522, 'Paris', 'City', 105.4, 'Temperate Oceanic', 35),
    (37.7749, -122.4194, 'San Francisco', 'City', 600.6, 'Mediterranean', 52);

-- Location Country
INSERT INTO LCountry (Latitude, Longitude, Country)
VALUES
    (40.7128, -74.0060, 'United States'),
    (51.5074, -0.1278, 'United Kingdom'),
    (35.6895, 139.6917, 'Japan'),
    (19.4326, -99.1332, 'Mexico'),
    (48.8566, 2.3522, 'France'),
    (37.7749, -122.4194, 'United States');


-- Habitat
INSERT INTO Habitat (HabitatName, HabitatType, ConservationStatus, DegradationLevel, Latitude, Longitude)
VALUES 
    ('Central Park', 'Urban Park', 'Stable', 'Low', 40.7128, -74.0060),
    ('Hyde Park', 'Urban Park', 'Declining', 'Moderate', 51.5074, -0.1278),
    ('Ueno Park', 'Urban Park', 'Endangered', 'High', 35.6895, 139.6917),
    ('Bosque de Chapultepec', 'Urban Park', 'Stable', 'Low', 19.4326, -99.1332),
    ('Jardin des Tuileries', 'Urban Park', 'Declining', 'Moderate', 48.8566, 2.3522),
    ('Golden Gate Park', 'Urban Park', 'Endangered', 'High', 37.7749, -122.4194);

-- Habitat Threats
INSERT INTO HThreats (HabitatName, Threat)
VALUES 
    ('Central Park', 'Overuse'),
    ('Hyde Park', 'Pollution'),
    ('Ueno Park', 'Climate Change'),
    ('Bosque de Chapultepec', 'Invasive Species'),
    ('Jardin des Tuileries', 'Habitat Loss'),
    ('Golden Gate Park', 'Overuse');

-- Species
INSERT INTO Species (ScientificName, CommonName, ConservationStatus, GeographicDistribution)
VALUES 
    ('Panthera tigris', 'Tiger', 'Endangered', 'Asia'),
    ('Ailuropoda melanoleuca', 'Giant panda', 'Endangered', 'China'),
    ('Gorilla beringei', 'Mountain gorilla', 'Endangered', 'Africa'),
    ('Pongo pygmaeus', 'Orangutan', 'Critically endangered', 'Indonesia and Malaysia'),
    ('Elephas maximus', 'Asian elephant', 'Endangered', 'Asia'),
    ('Tursiops truncatus', 'Bottlenose dolphin', 'Least concern', 'Worldwide'),
    ('Canis lupus', 'Gray wolf', 'Least concern', 'North America, Eurasia'),
    ('Phoenicopterus roseus', 'Greater flamingo', 'Least concern', 'Africa, southern Europe to south-west Asia'),
    ('Felis catus', 'Domestic cat', 'Least concern', 'Worldwide'),
    ('Homo sapiens', 'Human', 'Not evaluated', 'Worldwide');

-- Species Threats
INSERT INTO SThreats (ScientificName, Threat)
VALUES 
    ('Panthera tigris', 'Habitat loss and fragmentation'),
    ('Ailuropoda melanoleuca', 'Habitat loss and fragmentation'),
    ('Gorilla beringei', 'Habitat loss and degradation'),
    ('Pongo pygmaeus', 'Habitat loss and fragmentation'),
    ('Elephas maximus', 'Habitat loss and fragmentation'),
    ('Tursiops truncatus', 'Habitat loss and degradation'),
    ('Canis lupus', 'Habitat loss and fragmentation'),
    ('Phoenicopterus roseus', 'Habitat loss and degradation'),
    ('Felis catus', 'Predation and competition'),
    ('Homo sapiens', 'Habitat loss, fragmentation and degradation');



-- Population
INSERT INTO Population (PopulationID, Size, Trend, GrowthRate, Density, HabitatName, SpeciesScientificName)
VALUES
    (1, 1000, 'Decreasing', -0.05, 10.0, 'Central Park', 'Panthera tigris'),
    (2, 5000, 'Stable', 0.0, 25.0, 'Golden Gate Park', 'Gorilla beringei'),
    (3, 250, 'Increasing', 0.1, 2.5, 'Hyde Park', 'Phoenicopterus roseus'),
    (4, 15000, 'Stable', 0.0, 5.0, 'Ueno Park', 'Ailuropoda melanoleuca'),
    (5, 100, 'Decreasing', -0.1, 0.5, 'Jardin des Tuileries', 'Pongo pygmaeus');

-- Researcher
INSERT INTO Researcher (Name, Email, Phone, Expertise, SpeciesScientificName, PopulationID)
VALUES 
    ('John Doe', 'johndoe@example.com', '555-1234', 'Ornithology', 'Panthera tigris', 1),
    ('Jane Smith', 'janesmith@example.com', '555-5678', 'Herpetology', 'Gorilla beringei', 2),
    ('Bob Johnson', 'bjohnson@example.com', '555-9012', 'Mammalogy', 'Canis lupus', NULL);

-- AssistantResearcher
INSERT INTO AssistantResearcher (Name, Email, ResearcherEmail)
VALUES 
    ('Alice Brown', 'alicebrown@example.com', 'janesmith@example.com'),
    ('Tom Lee', 'tomlee@example.com', 'johndoe@example.com');

-- RProjects
INSERT INTO RProjects (Email, Project)
VALUES 
    ('janesmith@example.com', 'Conservation of T. carolina population in the wild'),
    ('johndoe@example.com', 'Study of Corvus corax nesting behavior');

-- RInterests
INSERT INTO RInterests (Email, ResearchInterests)
VALUES 
    ('johndoe@example.com', 'Bird migration patterns'),
    ('janesmith@example.com', 'Amphibian habitat preferences');

-- UniversityResearcher
INSERT INTO UniversityResearcher (Name, UniversityName, Tenure, Email)
VALUES 
    ('Sarah Brown', 'University of California, Berkeley', 'Assistant Professor', 'bjohnson@example.com'),
    ('Mark Lee', 'University of Michigan', 'Associate Professor', 'janesmith@example.com');

-- CompanyResearcher
INSERT INTO CompanyResearcher (Name, CompanyName, JobTitle, Email)
VALUES 
    ('Jennifer Johnson', 'Acme Inc.', 'Senior Biologist', 'johndoe@example.com');
