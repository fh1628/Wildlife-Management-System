CREATE SCHEMA WILDLIFE_SCHEMA;

USE WILDLIFE_SCHEMA;


DELIMITER //

CREATE PROCEDURE CREATE_LOCATION_TABLE()
BEGIN
	CREATE TABLE Location (
	  Latitude FLOAT NOT NULL,
	  Longitude FLOAT NOT NULL,
	  LocationName VARCHAR(255),
	  LocationType VARCHAR(50),
	  Area FLOAT,
	  Climate VARCHAR(50),
	  Elevation FLOAT,
	  PRIMARY KEY (Latitude, Longitude)
	);

	CREATE TABLE LCountry (
	  Latitude FLOAT NOT NULL,
	  Longitude FLOAT NOT NULL,
	  Country VARCHAR(50),
	  FOREIGN KEY (Latitude, Longitude) REFERENCES Location (Latitude, Longitude) ON DELETE CASCADE,
	  PRIMARY KEY(Latitude, Longitude, Country)
	);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE CREATE_HABITAT_TABLE()
BEGIN
	CREATE TABLE Habitat (
	  HabitatName VARCHAR(255) PRIMARY KEY,
	  HabitatType VARCHAR(50),
	  ConservationStatus VARCHAR(50),
	  DegradationLevel VARCHAR(50),
	  Latitude FLOAT,
	  Longitude FLOAT,
	  FOREIGN KEY (Latitude, Longitude) REFERENCES Location (Latitude, Longitude) ON DELETE CASCADE
	);

	CREATE TABLE HThreats (
	  HabitatName VARCHAR(255), 
	  Threat VARCHAR(255),
	  FOREIGN KEY (HabitatName) REFERENCES Habitat(HabitatName) ON DELETE CASCADE,
	  PRIMARY KEY(HabitatName, Threat)
	);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE CREATE_POPULATION_TABLE()
BEGIN
	CREATE TABLE Population (
	  PopulationID INT PRIMARY KEY,
	  Size INT,
	  Trend VARCHAR(50),
	  GrowthRate DECIMAL(5, 2),
	  Density DECIMAL(10, 2),
	  HabitatName VARCHAR(255),
	  SpeciesScientificName VARCHAR(255),
	  FOREIGN KEY (HabitatName) REFERENCES Habitat(HabitatName) ON DELETE CASCADE,
	  FOREIGN KEY (SpeciesScientificName) REFERENCES Species(ScientificName) ON DELETE CASCADE
	);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE CREATE_SPECIES_TABLE()
BEGIN
	CREATE TABLE Species (
	  ScientificName VARCHAR(255) PRIMARY KEY,
	  CommonName VARCHAR(255),
	  ConservationStatus VARCHAR(50),
	  GeographicDistribution VARCHAR(255)
	);

	CREATE TABLE SThreats (
	  ScientificName VARCHAR(255), 
	  Threat VARCHAR(255),
	  FOREIGN KEY (ScientificName) REFERENCES Species(ScientificName) ON DELETE CASCADE,
	  PRIMARY KEY(ScientificName, Threat)
	);
END //

DELIMITER ;

DELIMITER //

DELIMITER // 

CREATE PROCEDURE CREATE_RESEARCHER_TABLE()
BEGIN
	CREATE TABLE Researcher (
	  Name VARCHAR(255),
	  Email VARCHAR(255) PRIMARY KEY,
	  Phone VARCHAR(255),
	  Expertise VARCHAR(255),
	  SpeciesScientificName VARCHAR(255),
	  PopulationID INT,
	  FOREIGN KEY (PopulationID) REFERENCES Population (PopulationID) ON DELETE SET NULL
	);

	CREATE TABLE AssistantResearcher (
	  Name VARCHAR(255),
	  Email VARCHAR(255),
	  ResearcherEmail VARCHAR(255),
	  FOREIGN KEY (ResearcherEmail) REFERENCES Researcher(Email) ON DELETE CASCADE,
	  PRIMARY KEY (ResearcherEmail, Email)
	);

	CREATE TABLE RProjects (
	  Email VARCHAR(255),
	  Project VARCHAR(255),
	  FOREIGN KEY (Email) REFERENCES Researcher(Email) ON DELETE CASCADE,
	  PRIMARY KEY(Email, Project)
	);

	CREATE TABLE RInterests (
	  Email VARCHAR(255),
	  ResearchInterests VARCHAR(50),
	  FOREIGN KEY (Email) REFERENCES Researcher(Email) ON DELETE CASCADE,
	  PRIMARY KEY (Email, ResearchInterests)
	);

	CREATE TABLE UniversityResearcher (
	  Name VARCHAR(255),
	  UniversityName VARCHAR(255),
	  Tenure VARCHAR(255),
	  Email VARCHAR(255) PRIMARY KEY,
	  FOREIGN KEY (Email) REFERENCES Researcher(Email) ON DELETE CASCADE
	);

	CREATE TABLE CompanyResearcher (
	  Name VARCHAR(255),
	  CompanyName VARCHAR(255),
	  JobTitle VARCHAR(255),
	  Email VARCHAR(255) PRIMARY KEY,
	  FOREIGN KEY (Email) REFERENCES Researcher(Email) ON DELETE CASCADE
	);
END //

DELIMITER ;


