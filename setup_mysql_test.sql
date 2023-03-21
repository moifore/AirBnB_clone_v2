-- Creates a MySQL server with:
--	Database: hbnb_test_db
--	User: hbnb_test
--	Password: hbnb_test_pwd

--   Grants all privileges for hbnb_dev on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance_schema.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
