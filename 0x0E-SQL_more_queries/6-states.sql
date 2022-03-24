-- Creates a database `hbtn_0d_usa` and table `states`
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
