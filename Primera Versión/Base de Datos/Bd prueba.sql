-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dbpython
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dbpython
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbpython` DEFAULT CHARACTER SET latin1 ;
USE `dbpython` ;

-- -----------------------------------------------------
-- Table `dbpython`.`login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`login` (
  `idLogin` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(25) NOT NULL,
  `apellido` VARCHAR(25) NOT NULL,
  `usuario` VARCHAR(25) NOT NULL,
  `clave` VARCHAR(25) NOT NULL,
  `tipo` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`idLogin`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `dbpython`.`trabajos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbpython`.`trabajos` (
  `idtrabajo` INT NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `materia` VARCHAR(45) NOT NULL,
  `carrera` VARCHAR(45) NOT NULL,
  `idLogin` INT(11) NOT NULL,
  PRIMARY KEY (`idtrabajo`),
  INDEX `fk_trabajos_login_idx` (`idLogin` ASC),
  CONSTRAINT `fk_trabajos_login`
    FOREIGN KEY (`idLogin`)
    REFERENCES `dbpython`.`login` (`idLogin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


insert into Login values (1,'Jose','Fernandez','user1','h','Profesor');

SELECT nombre, apellido FROM Login WHERE usuario = 'user1' AND clave = 'h';