-- create a user table with id, email, name, and country columns
DROP TABLE IF EXISTS user;
CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
