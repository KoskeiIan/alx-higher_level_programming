-- Creates table `unique_id` on the server
CREATE TABLE IF OT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
