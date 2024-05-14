-- creates index on first letter of column `name` and `score`.
CREATE INDEX idx_name_first_score ON names (name(1), score);
