-- script to index the first letter of `name` of the table 'names'
CREATE INDEX idx_name_first ON names (name(1));
