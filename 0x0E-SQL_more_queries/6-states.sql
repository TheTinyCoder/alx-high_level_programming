-- create table with autoincrement id which is the primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY AUTOINCREMENT, name VARCHAR(256) NOT NULL);
