-- Trigger to decrease quantity of an item after placing a new order.
DELIMITER $$
CREATE TRIGGER decrease_item_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;
$$
DELIMITER ;
