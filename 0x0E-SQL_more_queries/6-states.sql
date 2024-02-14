-- create a database hbtn_0d_usa
-- create a table states in hbtn_0d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(256)
    )
