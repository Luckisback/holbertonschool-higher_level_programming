-- A script that creates a database + a table with a primary and foreign key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities ( 
		id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL, 
		state_id INT NOT NULL, 
		FOREIGN KEY (state_id) REFERENCES states (id)
		name VARCHAR(256) NOT NULL,);
