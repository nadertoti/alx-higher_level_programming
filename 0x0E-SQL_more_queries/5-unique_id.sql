-- create new table on database
CREATE TABLE IF NOT EXISTS `unique_id`
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
