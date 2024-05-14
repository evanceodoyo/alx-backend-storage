-- Stored procedure that adds a new correction for a student
CREATE TABLE IF NOT EXISTS projects (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT
)
BEGIN
	DECLARE project_id INT;
	SELECT id INTO project_id FROM projects WHERE name = project_name;

	IF project_id > 0 THEN
		INSERT INTO corrections (user_id, project_id, score) VALUES (
			user_id, project_id, score
		);
	ELSE
		INSERT INTO projects (name) VALUES (project_name);
		SET @new_project_id = LAST_INSERT_ID();
		INSERT INTO corrections (user_id, project_id, score) VALUES (
			user_id, @new_project_id, score
		);
	END IF;
END$$
DELIMITER ;
