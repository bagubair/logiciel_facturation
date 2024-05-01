CREATE TABLE IF NOT EXISTS artisant(
    ID SERIAL INT PRIMARY KEY,
    nom_entreprise VARCHAR(30),
    adresse VARCHAR(50),
    telephone VARCHAR(15),
    mail VARCHAR(25);)

CREATE TABLE IF NOT EXISTS client(
    ID SERIAL INT PRIMARY KEY,
    nom VARCHAR(15),
    prenom VARCHAR(15),
    adresse VARCHAR(50),
    telephone VARCHAR(15),
    mail VARCHAR(25);)

CREATE TABLE IF NOT EXISTS intervention(
    ID SERIAL INT PRIMARY KEY,
    type_intervention VARCHAR(50),
    date_service date,
    description VARCHAR(150),
    prix INT,
    materiaux_utilises VARCHAR(100);)