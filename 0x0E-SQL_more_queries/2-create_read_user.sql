-- creates a database hbtn_0d_2 and code should not fail if the DB exist
-- creates a user user_0d_2 and code should not fail if user exist
-- grant SELECT privileges to user_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
