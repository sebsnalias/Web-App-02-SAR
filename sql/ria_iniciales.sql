DROP DATABASE IF EXISTS ria_iniciales;
CREATE DATABASE ria_iniciales;

USE ria_iniciales;

CREATE TABLE clientes(
	nombre varchar(50) NOT NULL PRIMARY KEY,
	ap_paterno varchar(50) NOT NULL,
	ap_materno varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	direccion varchar(50) NOT NULL
)ENGINE = InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE productos(
	nombre_prod varchar(50)	NOT NULL PRIMARY KEY,
	tipo varchar(50) NOT NULL,
	descripcion varchar(50) NOT NULL,
	marca varchar(50) NOT NULL,
	origen varchar (15) NOT NULL
)ENGINE = InnoDB DEFAULT CHARSET=latin1;

INSERT INTO clientes(nombre,ap_paterno,ap_materno,email,direccion)
VALUES ('Linda','Silva','Ramirez','lindasilra@email','Ocampo #53'),
('Tomas','Rousseau','DosSantos','tom1945@email','Libertad #13'),
('Ana','Lopez','Mateos','aloteos@email','Arboledas #25');

INSERT INTO productos(nombre_prod,tipo,descripcion,marca,origen)
VALUES ('Leche','alimento','Leche 100% pura de vaca','alpura','Mexico'),
('huevos','alimento','Huevos de rancho','Don huevo','Mexico'),
('sandalias','calzado','Las mejores de la zona','Sandi','China');

SHOW TABLES;

SELECT * FROM clientes;

DESCRIBE clientes;

SELECT * FROM productos;

DESCRIBE productos;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;