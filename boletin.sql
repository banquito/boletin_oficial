-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: boletin
-- ------------------------------------------------------
-- Server version	5.5.31-0ubuntu0.12.04.1

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
-- Table structure for table `adjudicacion`
--

DROP TABLE IF EXISTS `adjudicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adjudicacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `objeto` text COLLATE utf8_bin,
  `texto_original` text COLLATE utf8_bin,
  `reparticion_id` int(11) DEFAULT NULL,
  `boletin_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reparticion_id` (`reparticion_id`),
  KEY `boletin_id` (`boletin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15733 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `articulo`
--

DROP TABLE IF EXISTS `articulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `articulo` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `texto` text,
  PRIMARY KEY (`id`),
  KEY `id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16903 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `boletin`
--

DROP TABLE IF EXISTS `boletin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `boletin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seccion` varchar(2) COLLATE utf8_bin DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1350 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dependencia`
--

DROP TABLE IF EXISTS `dependencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dependencia` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nombre` text,
  PRIMARY KEY (`id`),
  KEY `puestos_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19541 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `designacion`
--

DROP TABLE IF EXISTS `designacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `designacion` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `persona_id` int(50) DEFAULT NULL,
  `dependencia_id` int(50) DEFAULT NULL,
  `puesto_id` int(50) DEFAULT NULL,
  `articulo_id` int(50) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `persona_id` (`persona_id`),
  KEY `dependencia_id` (`dependencia_id`),
  KEY `puesto_id` (`puesto_id`),
  KEY `puestos_id_index` (`id`),
  KEY `fk_articulos` (`articulo_id`),
  CONSTRAINT `designacion_ibfk_1` FOREIGN KEY (`persona_id`) REFERENCES `persona_2` (`id`),
  CONSTRAINT `designacion_ibfk_2` FOREIGN KEY (`dependencia_id`) REFERENCES `dependencia` (`id`),
  CONSTRAINT `designacion_ibfk_3` FOREIGN KEY (`puesto_id`) REFERENCES `puesto` (`id`),
  CONSTRAINT `designacion_ibfk_4` FOREIGN KEY (`articulo_id`) REFERENCES `articulo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16903 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `oferente`
--

DROP TABLE IF EXISTS `oferente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oferente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `precio` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `sociedad_id` int(11) DEFAULT NULL,
  `adjudicacion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sociedad_id` (`sociedad_id`),
  KEY `adjudicacion_id` (`adjudicacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23972 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persona` (
  `per_id` int(11) NOT NULL AUTO_INCREMENT,
  `per_nombre` text,
  `per_apellido` text,
  `per_nya` text NOT NULL,
  `per_titulo` varchar(255) DEFAULT NULL,
  `per_prefijo` varchar(255) DEFAULT NULL,
  `per_sufijo` varchar(255) DEFAULT NULL,
  `per_cuit` int(11) DEFAULT NULL,
  `per_dni` int(11) DEFAULT NULL,
  `per_estado_civil` varchar(255) DEFAULT NULL,
  `per_domicilio_especial` varchar(255) DEFAULT NULL,
  `per_boletines` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`per_id`),
  UNIQUE KEY `pf` (`per_nya`(255),`per_dni`)
) ENGINE=MyISAM AUTO_INCREMENT=424869 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `persona_2`
--

DROP TABLE IF EXISTS `persona_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persona_2` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `codigo_tipo` varchar(10) DEFAULT NULL,
  `codigo_numero` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `puestos_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14461 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `puesto`
--

DROP TABLE IF EXISTS `puesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `puesto` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nombre` text,
  PRIMARY KEY (`id`),
  KEY `puestos_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7395 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reparticion`
--

DROP TABLE IF EXISTS `reparticion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reparticion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` text COLLATE utf8_bin,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=15835 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sociedad`
--

DROP TABLE IF EXISTS `sociedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sociedad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` text NOT NULL,
  `soc_fantasia` varchar(255) DEFAULT NULL,
  `soc_tipo_social` int(11) DEFAULT NULL,
  `soc_domicilio_especial` varchar(255) DEFAULT NULL,
  `soc_involucrados` varchar(255) DEFAULT NULL,
  `soc_descripcion` text,
  `soc_adjuntos` varchar(255) DEFAULT NULL,
  `soc_titulo` varchar(255) DEFAULT NULL,
  `soc_latlon` varchar(255) DEFAULT NULL,
  `soc_rdf` varchar(255) DEFAULT NULL,
  `soc_hash` varchar(255) DEFAULT NULL,
  `filename` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=184663 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sociedad_involucrados`
--

DROP TABLE IF EXISTS `sociedad_involucrados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sociedad_involucrados` (
  `si_id` int(11) NOT NULL AUTO_INCREMENT,
  `si_fk_id` int(11) NOT NULL,
  `si_involucrados` int(11) NOT NULL,
  `si_extra` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`si_id`),
  UNIQUE KEY `si_fk_id_2` (`si_fk_id`,`si_involucrados`),
  KEY `si_fk_id` (`si_fk_id`)
) ENGINE=MyISAM AUTO_INCREMENT=724229 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-11-04 17:09:14