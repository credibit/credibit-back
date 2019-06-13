INSERT INTO creditRequest (nombreEmpresa, correo, puntosBuro, puntosSat,\
            ingresoMensual, ingresoNeto, cantidadDeseada, plazoDeseado, companySite,\
            toPay, approved, twitter, linkedin, facebook, founded, employees

CREATE TABLE creditRequest (
    nombreEmpresa VARCHAR(256) NOT NULL,
    correo VARCHAR(256) NOT NULL,
    puntosBuro INT NOT NULL,
    puntosSat INT NOT NULL,
    ingresoMensual FLOAT NOT NULL,
    ingresoNeto FLOAT NOT NULL,
    cantidadDeseada FLOAT NOT NULL,
    plazoDeseado INT NOT NULL,
    companySite VARCHAR(256) NOT NULL,
    toPay FLOAT NOT NULL,
    approved TINYINT(1),
    twitter VARCHAR(256),
    linkedin VARCHAR(256),
    facebook VARCHAR(256),
    founded INT,
    employees INT
)Engine=InnoDB;

CREATE TABLE admin (
    username VARCHAR(256) NOT NULL KEY,
    password VARCHAR(256) NOT NULL
)Engine=InnoDB;

INSERT INTO admin (username, password) VALUES ("luis", "1234");
INSERT INTO admin (username, password) VALUES ("dafne", "diego");