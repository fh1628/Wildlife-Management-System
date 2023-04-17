-- Researcher Table order researchers based on scientific species name
CREATE INDEX idx_Researcher_on_Scientific_Name ON Researcher (SpeciesScientificName);

-- Population Table 
-- CREATE INDEX idx_Population_on_Scientific_Name ON Population (SpeciesScientificName);
CREATE INDEX idx_Population_on_Habitat_Name ON Population (HabitatName);

-- Species Table: index on scientific name to help with query 1
CREATE INDEX idx_Species_on_Scientific_Name ON Species (ScientificName);