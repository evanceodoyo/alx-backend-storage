-- Creates as stored procedure that computes and stores the average weighted
-- score for a students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE result FLOAT;


	UPDATE users
		SET users.average_score = (
		   SELECT SUM(score * weight) / SUM(weight)
                	FROM corrections
                	INNER JOIN projects
                	ON corrections.project_id = projects.id
                	WHERE corrections.user_id = users.id
		);
END$$
DELIMITER ;
