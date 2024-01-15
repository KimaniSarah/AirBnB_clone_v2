-- Create a database and a new user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
