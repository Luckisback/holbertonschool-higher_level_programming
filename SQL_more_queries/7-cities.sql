-- A script that creates a database + a table with a primary and foreign key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
		id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
		name VARCHAR(256) NOT NULL,
		state_id INT FOREIGN KEY REFERENCE states (id));
