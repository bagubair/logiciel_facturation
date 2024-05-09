
CREATE TABLE IF NOT EXISTS utilisateur(
    ID SERIAL PRIMARY KEY,
    prenom VARCHAR(30),
    nom VARCHAR(30),
    nom_utilisateur VARCHAR(30),
    mot_passe VARCHAR(30),
    tel VARCHAR(15)
);
CREATE TABLE IF NOT EXISTS entreprise(
    nom_entreprise VARCHAR(30),
    adresse TEXT,
    mail VARCHAR(25),
    telephone VARCHAR(20),
    nb_ser VARCHAR(20),
    logo TEXT,
    id_utilisateur INT REFERENCES utilisateur(ID) PRIMARY KEY -- ici referance a table utilisature ,, et prend la valeur de collon nom utilisateur , on relie chaque facture par l'artisant (entrprise)
);

CREATE TABLE IF NOT EXISTS client(
    num VARCHAR(15) , -- numero de client commence par CL donc c'est une VARCHAR
    nom VARCHAR(25),
    prenom VARCHAR(25),
    adresse TEXT,
    tel_fax VARCHAR(20),
    mobil VARCHAR(20),
    coment TEXT,
    id_utilisateur INT REFERENCES utilisateur(ID), -- ici referance a table utilisature ,, et prend la valeur de collon nom utilisateur , on relie l'utilisature avec ces clients 
    PRIMARY KEY(num, id_utilisateur)
);


CREATE TABLE IF NOT EXISTS facture(
    num VARCHAR(15),  -- numero de facture commence par FAC donc c'est une VARCHAR
    date_fac VARCHAR(20),  -- c'est une VARCHAR cet entree par Entry 
    intervens TEXT, --ici tous les interventios de la facture ,, sra dans un lise , mais on va metre ici en type str 
    remarque TEXT,
    etat_fac INT,
    net_pay INT,
    info_pay TEXT,  -- il eura la date d'echnge et mod de pay
    infos_banque TEXT,
    sign TEXT,
    id_utilisateur INT REFERENCES utilisateur(ID) , -- ici referance a table utilisature ,, et prend la valeur de collon nom utilisateur , on relie chaque facture par l'artisant(entrprise )
    ref_client VARCHAR(15), -- ici referance au client , pren num client
    PRIMARY KEY(num, id_utilisateur),
    FOREIGN KEY (ref_client, id_utilisateur) REFERENCES client(num, id_utilisateur)
);
/*

CREATE TABLE IF NOT EXISTS intervention(
    ID SERIAL INT PRIMARY KEY,
    type_intervention VARCHAR(50),
    date_service date,
    description VARCHAR(150),
    prix INT,
    materiaux_utilises VARCHAR(100);)

*/