-- A script that creates a database + a table with a primary and foreign key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities ( 
		id INT UNIQUE AUTO_INCREMENT NOT NULL, 
		state_id INT NOT NULL,
		name VARCHAR(256) NOT NULL,
		PRIMARY KEY (id),
		FOREIGN KEY (state_id) REFERENCES states (id));
