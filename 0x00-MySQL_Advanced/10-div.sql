-- creates a function that divides (and returns) the first by the second
-- number or returns 0 if the second number is equal to 0.
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
READS SQL DATA
BEGIN
	RETURN (
		IF(b = 0, 0, a / b)
	);
END$$
DELIMITER ;
