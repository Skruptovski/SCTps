-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: dbpython
-- ------------------------------------------------------
-- Server version	5.7.15-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actividades`
--

DROP TABLE IF EXISTS `actividades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `actividades` (
  `idTrabajo` int(11) NOT NULL,
  `consigna` varchar(250) NOT NULL,
  `respuesta1` varchar(250) NOT NULL,
  `respuesta2` varchar(250) NOT NULL,
  `respuesta3` varchar(250) NOT NULL,
  `correcta` int(11) NOT NULL,
  KEY `fk_enunciado_trabajos1` (`idTrabajo`),
  CONSTRAINT `fk_enunciado_trabajos1` FOREIGN KEY (`idTrabajo`) REFERENCES `trabajos` (`idTrabajo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividades`
--

LOCK TABLES `actividades` WRITE;
/*!40000 ALTER TABLE `actividades` DISABLE KEYS */;
INSERT INTO `actividades` VALUES (1,'Ejemplo consigna trabajo 001','Respuesta 1  ejemplo 001','Respuesta 2 ejemplo 001 (correcta)','Respuesta 3 ejemplo 001',2);
/*!40000 ALTER TABLE `actividades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peticiones`
--

DROP TABLE IF EXISTS `peticiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `peticiones` (
  `idPeticion` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`idPeticion`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peticiones`
--

LOCK TABLES `peticiones` WRITE;
/*!40000 ALTER TABLE `peticiones` DISABLE KEYS */;
INSERT INTO `peticiones` VALUES (1,'g','g','u','g'),(2,'oo','jj','55','nn'),(3,'as','ds','cx','qw');
/*!40000 ALTER TABLE `peticiones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajos`
--

DROP TABLE IF EXISTS `trabajos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trabajos` (
  `idTrabajo` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(45) NOT NULL,
  `materia` varchar(45) NOT NULL,
  `carrera` varchar(45) NOT NULL,
  `usuario` varchar(45) NOT NULL,
  PRIMARY KEY (`idTrabajo`),
  KEY `fk_trabajos_usuarios1_idx` (`usuario`),
  CONSTRAINT `fk_trabajos_usuarios1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajos`
--

LOCK TABLES `trabajos` WRITE;
/*!40000 ALTER TABLE `trabajos` DISABLE KEYS */;
INSERT INTO `trabajos` VALUES (1,'tp001ejemplo','proyecto de software','sistemas','prueba@gmail.com'),(2,'','','','prueba@gmail.com'),(3,'','','','prueba@gmail.com'),(4,'','','','prueba@gmail.com'),(5,'','','','prueba@gmail.com'),(6,'','','','prueba@gmail.com'),(7,'','','','prueba@gmail.com'),(8,'','','','prueba@gmail.com'),(9,'','','','prueba@gmail.com'),(10,'','','','prueba@gmail.com'),(11,'','','','prueba@gmail.com'),(12,'','','','prueba@gmail.com'),(13,'','','','prueba@gmail.com'),(14,'','','','prueba@gmail.com'),(15,'','','','prueba@gmail.com'),(16,'','','','prueba@gmail.com'),(17,'','','','prueba@gmail.com'),(18,'','','','prueba@gmail.com'),(19,'','','','prueba@gmail.com'),(20,'','','','prueba@gmail.com'),(21,'','','','prueba@gmail.com'),(22,'','','','prueba@gmail.com');
/*!40000 ALTER TABLE `trabajos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `usuario` varchar(45) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `clave` varchar(25) NOT NULL,
  `tipo` varchar(25) NOT NULL,
  PRIMARY KEY (`usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES ('prueba2@gmail.com','Prueba','S','1234','Admin'),('prueba@gmail.com','Prueba','V','1234','Docente');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuariosxpeticiones`
--

DROP TABLE IF EXISTS `usuariosxpeticiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuariosxpeticiones` (
  `usuario` varchar(45) NOT NULL,
  `idPeticion` int(11) NOT NULL,
  PRIMARY KEY (`usuario`,`idPeticion`),
  KEY `fk_usuarios_has_peticiones_peticiones1_idx` (`idPeticion`),
  KEY `fk_usuarios_has_peticiones_usuarios1_idx` (`usuario`),
  CONSTRAINT `fk_usuarios_has_peticiones_peticiones1` FOREIGN KEY (`idPeticion`) REFERENCES `peticiones` (`idPeticion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_peticiones_usuarios1` FOREIGN KEY (`usuario`) REFERENCES `usuarios` (`usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuariosxpeticiones`
--

LOCK TABLES `usuariosxpeticiones` WRITE;
/*!40000 ALTER TABLE `usuariosxpeticiones` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuariosxpeticiones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-06 14:24:28
