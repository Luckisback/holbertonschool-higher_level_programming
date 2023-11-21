-- A script that creates the database "hbtn_0d_usa" and the table "states"

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256) NOT NULL
);
