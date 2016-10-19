-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema travelkeepdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema travelkeepdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `travelkeepdb` DEFAULT CHARACTER SET utf8 ;
USE `travelkeepdb` ;

-- -----------------------------------------------------
-- Table `travelkeepdb`.`trips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`trips` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  `rating` TINYINT(1) NULL DEFAULT NULL,
  `start_location` VARCHAR(45) NULL DEFAULT NULL,
  `end_location` VARCHAR(45) NULL DEFAULT NULL,
  `trip_miles` INT(11) NULL DEFAULT NULL,
  `trip_complete` INT(1) NULL DEFAULT '0',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `share_w_friends` TINYINT(1) NULL DEFAULT NULL,
  `picture` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  `trip_id` INT(11) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  INDEX `fk_comments_trips1_idx` (`trip_id` ASC),
  CONSTRAINT `fk_comments_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`favorites` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `trip_id` INT(11) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `favorite_status` TINYINT(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorites_users1_idx` (`user_id` ASC),
  INDEX `fk_favorites_trips1_idx` (`trip_id` ASC),
  CONSTRAINT `fk_favorites_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`friends` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  `friend_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_friends_users_a_idx` (`user_id` ASC),
  INDEX `fk_friends_users_b_idx` (`friend_id` ASC),
  CONSTRAINT `fk_friends_users1_b`
    FOREIGN KEY (`friend_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_friends_users_a`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`participants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`participants` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `trip_id` INT(11) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_participants_users1_idx` (`user_id` ASC),
  INDEX `fk_participants_trips1_idx` (`trip_id` ASC),
  CONSTRAINT `fk_participants_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_participants_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `travelkeepdb`.`photos_vids`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `travelkeepdb`.`photos_vids` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `photo` VARCHAR(100) NULL DEFAULT NULL,
  `videos` VARCHAR(100) NULL DEFAULT NULL,
  `trip_id` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_photos_vids_trips1_idx` (`trip_id` ASC),
  INDEX `fk_photos_vids_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_photos_vids_trips1`
    FOREIGN KEY (`trip_id`)
    REFERENCES `travelkeepdb`.`trips` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_photos_vids_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `travelkeepdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
