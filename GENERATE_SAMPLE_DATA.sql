-- Location
INSERT INTO Location (Latitude, Longitude, LocationName, LocationType, Country, Area, Climate, Elevation)
VALUES
    (40.7128, -74.0060, 'New York City', 'City', 'United States', 468.9, 'Humid Subtropical', 10),
    (51.5074, -0.1278, 'London', 'City', 'United Kingdom', 1572, 'Temperate Maritime', 35),
    (35.6895, 139.6917, 'Tokyo', 'City', 'Japan', 2187, 'Humid Subtropical', 131),
    (19.4326, -99.1332, 'Mexico City', 'City', 'Mexico', 1485, 'Humid Subtropical', 2240),
    (48.8566, 2.3522, 'Paris', 'City', 'France', 105.4, 'Temperate Oceanic', 35),
    (37.7749, -122.4194, 'San Francisco', 'City', 'United States', 600.6, 'Mediterranean', 52),
    (-2.3326, 34.8255, 'Serengeti Plains', 'Savanna', 'Tanzania', 30000, 'Tropical', 1162),
    (-3.4653, -62.2159, 'Amazon Rainforest', 'Rainforest', 'Brazil', 706.7, 'Tropical', 200),
	(23.4162, 15.5377, 'Sahara Desert', 'Desert', 'Multiple', 9065000, 'Hot desert', 500),
    (32.5, 103.5, 'Minshan Mountains', 'Mountain', 'China', 70000, 'subtropical highland climate', 1000);
    


-- Habitat
INSERT INTO Habitat (HabitatName, HabitatType, ConservationStatus, DegradationLevel, Latitude, Longitude)
VALUES 
    ('Central Park', 'Urban Park', 'Stable', 'Low', 40.7128, -74.0060),
    ('Hyde Park', 'Urban Park', 'Declining', 'Moderate', 51.5074, -0.1278),
    ('Ueno Park', 'Urban Park', 'Endangered', 'High', 35.6895, 139.6917),
    ('Bosque de Chapultepec', 'Urban Park', 'Stable', 'Low', 19.4326, -99.1332),
    ('Jardin des Tuileries', 'Urban Park', 'Declining', 'Moderate', 48.8566, 2.3522),
    ('Golden Gate Park', 'Urban Park', 'Endangered', 'High', 37.7749, -122.4194),
    ('Serengeti Plains', 'Savanna', 'Stable', 'Low', -2.3326, 34.8255),
	('Amazon Rainforest', 'Tropical Rainforest', 'Declining', 'High', -3.4653, -62.2159),
	('Sahara Desert', 'Desert', 'Stable', 'Low', 23.4162, 15.5377),
    ('Mount Siguniang', 'Forest', 'Stable', 'Moderate', 32.5, 103.5),
    ('Mount Daxue', 'Forest', 'Stable', 'Moderate', 32.5, 103.5);
    

-- Habitat Threats
INSERT INTO HThreats (HabitatName, Threat)
VALUES 
    ('Central Park', 'Overuse'),
    ('Central Park', 'Pollusion'),
    ('Hyde Park', 'Pollution'),
    ('Ueno Park', 'Climate Change'),
    ('Ueno Park', 'Overuse'),
    ('Bosque de Chapultepec', 'Invasive Species'),
    ('Jardin des Tuileries', 'Habitat Loss'),
    ('Golden Gate Park', 'Overuse'),
    ('Mount Siguniang', 'Overuse'),
    ('Mount Daxue', 'Overuse');

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
    ('Homo sapiens', 'Human', 'Not evaluated', 'Worldwide'),
    ('Panthera uncia', 'Snow leopard', 'Vulnerable', 'Central and South Asia');

-- Species Threats
INSERT INTO SThreats (ScientificName, Threat)
VALUES 
    ('Panthera tigris', 'Habitat loss'),
    ('Panthera tigris', 'Fragmentation'),
    ('Ailuropoda melanoleuca', 'Habitat loss'),
    ('Gorilla beringei', 'Habitat loss'),
    ('Gorilla beringei', 'Degradation'),
    ('Pongo pygmaeus', 'Habitat loss'),
    ('Elephas maximus', 'Fragmentation'),
    ('Tursiops truncatus', 'Habitat loss'),
    ('Tursiops truncatus', 'Degradation'),
    ('Canis lupus', 'Habitat loss'),
    ('Phoenicopterus roseus', 'Habitat'),
    ('Felis catus', 'Predation'),
    ('Felis catus', 'Competition'),
    ('Homo sapiens', 'Degradation'),
    ('Panthera uncia', 'habitat loss'),
    ('Panthera uncia', 'poaching'),
    ('Panthera uncia', 'retaliatory killings');



-- Population
INSERT INTO Population (PopulationID, Size, Trend, GrowthRate, Density, HabitatName, SpeciesScientificName)
VALUES
    (1, 1000, 'Decreasing', -0.05, 10.0, 'Central Park', 'Panthera tigris'),
    (2, 5000, 'Stable', 0.0, 25.0, 'Golden Gate Park', 'Gorilla beringei'),
    (3, 250, 'Increasing', 0.1, 2.5, 'Hyde Park', 'Phoenicopterus roseus'),
    (4, 15000, 'Stable', 0.0, 5.0, 'Ueno Park', 'Ailuropoda melanoleuca'),
    (5, 1000, 'Increasing', 0.1, 1, 'Mount Siguniang', 'Ailuropoda melanoleuca'),
    (6, 500, 'Increasing', 0.07, 0.5, 'Mount Daxue', 'Ailuropoda melanoleuca'),
    (7, 2000, 'Decreasing', -0.05, 10.0, 'Mount Siguniang', 'Panthera uncia');
    
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


-- ConservationOrganization
INSERT INTO ConservationOrganization (ContactEmail, Name, Mission, Website)
VALUES
    ('GPCO124@mail.com', 'Giant Panda Conservation Organization', 'Protect the Endangered Giant Panda Population in China', 'www.GPCOChina.org' ),
    ('GorillaConservationor@example.com', 'African Mountain Gorilla Conservation Organization', 'Protect and help the Mountain Gorilla Population in Africa', 'www.MountainGorillaAfrica.com'),
    ('MMGPCO000@mail.com', 'Minshan Mountains Conservation Organization', 'Protect the Species that Live in Minshan Mountains', 'www.ProtectMinshanMountainsHabitants.org' );
    
-- Protects
INSERT INTO Protects (ContactEmail, PopulationID)
VALUES
	('GPCO124@mail.com', 5),
    ('GPCO124@mail.com', 6),
    ('MMGPCO000@mail.com', 5),
    ('MMGPCO000@mail.com', 7),
    ('GorillaConservationor@example.com',2);
    
    
    