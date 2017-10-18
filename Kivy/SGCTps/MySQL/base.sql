-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema sgctps
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sgctps
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sgctps` DEFAULT CHARACTER SET utf8 ;
USE `sgctps` ;

-- -----------------------------------------------------
-- Table `sgctps`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sgctps`.`usuario` (
  `Usuario` VARCHAR(10) NOT NULL,
  `DNI` VARCHAR(45) NOT NULL,
  `Contraseña` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `eMail` VARCHAR(45) NOT NULL,
  `Rol` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`Usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sgctps`.`trabajo_practico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sgctps`.`trabajo_practico` (
  `id_TP` INT(11) NOT NULL,
  `Titulo` VARCHAR(45) NOT NULL,
  `Materia` VARCHAR(45) NOT NULL,
  `Carrera` VARCHAR(45) NOT NULL,
  `Usuario_Usuario` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id_TP`),
  INDEX `fk_Trabajo_Practico_Usuario_idx` (`Usuario_Usuario` ASC),
  CONSTRAINT `fk_Trabajo_Practico_Usuario`
    FOREIGN KEY (`Usuario_Usuario`)
    REFERENCES `sgctps`.`usuario` (`Usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `sgctps`.`enunciado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sgctps`.`enunciado` (
  `id_Enunciado` INT(11) NOT NULL DEFAULT '1',
  `nroEnunciado` INT(2) NOT NULL,
  `Enunciado` VARCHAR(300) NOT NULL,
  `Respuesta1` VARCHAR(300) NOT NULL,
  `Respuesta2` VARCHAR(300) NOT NULL,
  `Respuesta3` VARCHAR(300) NOT NULL,
  `Correcta` INT(1) NOT NULL,
  `Trabajo_Practico_id_TP` INT(11) NOT NULL,
  PRIMARY KEY (`id_Enunciado`, `nroEnunciado`),
  INDEX `fk_Enunciado_Trabajo_Practico1_idx` (`Trabajo_Practico_id_TP` ASC),
  CONSTRAINT `fk_Enunciado_Trabajo_Practico1`
    FOREIGN KEY (`Trabajo_Practico_id_TP`)
    REFERENCES `sgctps`.`trabajo_practico` (`id_TP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
