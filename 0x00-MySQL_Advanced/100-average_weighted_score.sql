-- Creates as stored procedure that computes and stores the average weighted
-- score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weight_sum INT DEFAULT 0;
	DECLARE score_by_weight_sum FLOAT;
	
	SELECT SUM(score * weight),
		SUM(weight) 
		INTO score_by_weight_sum, weight_sum
		FROM corrections
		INNER JOIN projects 
		ON corrections.project_id = projects.id
		WHERE corrections.user_id = user_id;

	UPDATE users
		SET users.average_score = IF(
			weight_sum = 0, 0,
			score_by_weight_sum / weight_sum)
		WHERE users.id = user_id;
END$$
DELIMITER ;
