-- create table with a primary key and a foreign key linking to another table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT PRIMARY KEY AUTO_INCREMENT, state_id INT FOREIGN KEY REFERENCES states(id), name VARCHAR(256) NOT NULL);
