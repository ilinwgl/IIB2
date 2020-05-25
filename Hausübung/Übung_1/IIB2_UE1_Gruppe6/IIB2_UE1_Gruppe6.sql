-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: iib2_hue1_gruppe6
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gebaeude`
--

DROP TABLE IF EXISTS `gebaeude`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `gebaeude` (
  `ge_id` int(11) NOT NULL AUTO_INCREMENT,
  `ge_name` varchar(50) DEFAULT NULL,
  `ge_ort` varchar(50) DEFAULT NULL,
  `ge_plz` int(11) DEFAULT NULL,
  `ge_strasse` varchar(50) DEFAULT NULL,
  `ge_hausnummer` int(11) DEFAULT NULL,
  `ge_ifc_guid` int(11) DEFAULT NULL,
  PRIMARY KEY (`ge_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gebaeude`
--

LOCK TABLES `gebaeude` WRITE;
/*!40000 ALTER TABLE `gebaeude` DISABLE KEYS */;
INSERT INTO `gebaeude` VALUES (1,'Darmstadt Grundschule','Darmstadt',64287,'Luisenplatz',1,1);
/*!40000 ALTER TABLE `gebaeude` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `havc`
--

DROP TABLE IF EXISTS `havc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `havc` (
  `havc_id` int(11) NOT NULL AUTO_INCREMENT,
  `havc_name` varchar(50) DEFAULT NULL,
  `havc_typ` varchar(50) DEFAULT NULL,
  `havc_position` varchar(50) DEFAULT NULL,
  `havc_sw_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`havc_id`),
  KEY `havc_sw_id` (`havc_sw_id`),
  CONSTRAINT `havc_ibfk_1` FOREIGN KEY (`havc_sw_id`) REFERENCES `stockwerk` (`sw_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `havc`
--

LOCK TABLES `havc` WRITE;
/*!40000 ALTER TABLE `havc` DISABLE KEYS */;
INSERT INTO `havc` VALUES (1,'HVAC_Lüftung 1','Lüftungsanlage','Ebene 0',1),(2,'HVAC_Lüftung 2','Lüftungsanlage','Ebene 1',2),(3,'HAVC_Lüftung 3','Lüftungsanlage','Ebene 2',3);
/*!40000 ALTER TABLE `havc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `havcdaten`
--

DROP TABLE IF EXISTS `havcdaten`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `havcdaten` (
  `havcda_id` int(11) NOT NULL AUTO_INCREMENT,
  `havcda_zeitpunkt` datetime DEFAULT NULL,
  `havcda_stufe` varchar(50) DEFAULT NULL,
  `havcda_AnAusStatus` varchar(50) DEFAULT NULL,
  `havcda_havc_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`havcda_id`),
  KEY `havcda_havc_id` (`havcda_havc_id`),
  CONSTRAINT `havcdaten_ibfk_1` FOREIGN KEY (`havcda_havc_id`) REFERENCES `havc` (`havc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `havcdaten`
--

LOCK TABLES `havcdaten` WRITE;
/*!40000 ALTER TABLE `havcdaten` DISABLE KEYS */;
/*!40000 ALTER TABLE `havcdaten` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ln_besitzen`
--

DROP TABLE IF EXISTS `ln_besitzen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ln_besitzen` (
  `ln_bes_id` int(11) NOT NULL AUTO_INCREMENT,
  `ln_bes_ra_id` int(11) DEFAULT NULL,
  `ln_bes_wa_id` int(11) DEFAULT NULL,
  `ln_bes_wa_richtung` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ln_bes_id`),
  KEY `ln_bes_ra_id` (`ln_bes_ra_id`),
  KEY `ln_bes_wa_id` (`ln_bes_wa_id`),
  CONSTRAINT `ln_besitzen_ibfk_1` FOREIGN KEY (`ln_bes_ra_id`) REFERENCES `raum` (`ra_id`),
  CONSTRAINT `ln_besitzen_ibfk_2` FOREIGN KEY (`ln_bes_wa_id`) REFERENCES `wand` (`wa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ln_besitzen`
--

LOCK TABLES `ln_besitzen` WRITE;
/*!40000 ALTER TABLE `ln_besitzen` DISABLE KEYS */;
INSERT INTO `ln_besitzen` VALUES (1,1,1,'Ost'),(2,1,2,'Nord'),(3,1,3,'West'),(4,1,4,'Süd'),(5,2,3,'Ost'),(6,2,5,'Nord'),(7,2,6,'West'),(8,2,7,'Süd'),(9,3,6,'Ost'),(10,3,8,'Nord'),(11,3,9,'West'),(12,3,10,'Süd'),(13,4,11,'Ost'),(14,4,12,'Nord'),(15,4,13,'West'),(16,4,14,'Süd'),(17,5,13,'Ost'),(18,5,15,'Nord'),(19,5,16,'West'),(20,5,17,'Süd'),(21,6,16,'Ost'),(22,6,18,'Nord'),(23,6,19,'West'),(24,6,20,'Süd'),(25,7,21,'Ost'),(26,7,22,'Nord'),(27,7,23,'West'),(28,7,24,'Süd'),(29,8,23,'Ost'),(30,8,25,'Nord'),(31,8,26,'West'),(32,8,27,'Süd'),(33,9,26,'Ost'),(34,9,28,'Nord'),(35,9,29,'West'),(36,9,30,'Süd');
/*!40000 ALTER TABLE `ln_besitzen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ln_datenbearbeiten`
--

DROP TABLE IF EXISTS `ln_datenbearbeiten`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ln_datenbearbeiten` (
  `ln_dabe_id` int(11) NOT NULL AUTO_INCREMENT,
  `ln_dabe_per_id` int(11) DEFAULT NULL,
  `ln_dabe_ge_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`ln_dabe_id`),
  KEY `ln_dabe_per_id` (`ln_dabe_per_id`),
  KEY `ln_dabe_ge_id` (`ln_dabe_ge_id`),
  CONSTRAINT `ln_datenbearbeiten_ibfk_1` FOREIGN KEY (`ln_dabe_per_id`) REFERENCES `personen` (`per_id`),
  CONSTRAINT `ln_datenbearbeiten_ibfk_2` FOREIGN KEY (`ln_dabe_ge_id`) REFERENCES `gebaeude` (`ge_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ln_datenbearbeiten`
--

LOCK TABLES `ln_datenbearbeiten` WRITE;
/*!40000 ALTER TABLE `ln_datenbearbeiten` DISABLE KEYS */;
INSERT INTO `ln_datenbearbeiten` VALUES (1,1,1);
/*!40000 ALTER TABLE `ln_datenbearbeiten` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `multiusing`
--

DROP TABLE IF EXISTS `multiusing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `multiusing` (
  `mul_id` int(11) NOT NULL AUTO_INCREMENT,
  `mul_vorname` varchar(50) DEFAULT NULL,
  `mul_timestamp_vorname` datetime DEFAULT NULL,
  `mul_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mul_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `multiusing`
--

LOCK TABLES `multiusing` WRITE;
/*!40000 ALTER TABLE `multiusing` DISABLE KEYS */;
INSERT INTO `multiusing` VALUES (1,'Guanlin','2019-06-02 20:13:16','Wang');
/*!40000 ALTER TABLE `multiusing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personen`
--

DROP TABLE IF EXISTS `personen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `personen` (
  `per_id` int(11) NOT NULL AUTO_INCREMENT,
  `per_name` varchar(50) DEFAULT NULL,
  `per_vorname` varchar(50) DEFAULT NULL,
  `per_username` varchar(50) DEFAULT NULL,
  `per_passwort` blob,
  `per_beruf` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`per_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personen`
--

LOCK TABLES `personen` WRITE;
/*!40000 ALTER TABLE `personen` DISABLE KEYS */;
INSERT INTO `personen` VALUES (1,'Guanlin','Wang','WGL',_binary 'pbkdf2:sha256:150000$Fb3MiR3Q$2ee9effd9f5cf0e8aaf6dac2568ba2bbb3265ebdd43bd6f37a4fc1ab353c2900','Bauleiter');
/*!40000 ALTER TABLE `personen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raum`
--

DROP TABLE IF EXISTS `raum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `raum` (
  `ra_id` int(11) NOT NULL AUTO_INCREMENT,
  `ra_bezeichnung` varchar(50) DEFAULT NULL,
  `ra_ifc_guid` int(11) DEFAULT NULL,
  `ra_sw_id` int(11) DEFAULT NULL,
  `ra_nummer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ra_id`),
  KEY `ra_sw_id` (`ra_sw_id`),
  CONSTRAINT `raum_ibfk_1` FOREIGN KEY (`ra_sw_id`) REFERENCES `stockwerk` (`sw_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raum`
--

LOCK TABLES `raum` WRITE;
/*!40000 ALTER TABLE `raum` DISABLE KEYS */;
INSERT INTO `raum` VALUES (1,'Klassenraum',101,1,'001'),(2,'Klassenraum',102,1,'002'),(3,'Klassenraum',103,1,'003'),(4,'Lehrebüro',104,2,'101'),(5,'Lehrebüro',105,2,'102'),(6,'Lehrebüro',106,2,'103'),(7,'Kunst',107,3,'201'),(8,'Musik',108,3,'202'),(9,'Werk',109,3,'203');
/*!40000 ALTER TABLE `raum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor`
--

DROP TABLE IF EXISTS `sensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sensor` (
  `sen_id` int(11) NOT NULL AUTO_INCREMENT,
  `sen_name` varchar(50) DEFAULT NULL,
  `sen_typ` varchar(50) DEFAULT NULL,
  `sen_position` varchar(50) DEFAULT NULL,
  `sen_ra_id` int(11) DEFAULT NULL,
  `sen_havc_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sen_id`),
  KEY `sensor_ibfk_1` (`sen_ra_id`),
  KEY `sensor_ibfk_2` (`sen_havc_id`),
  CONSTRAINT `sensor_ibfk_1` FOREIGN KEY (`sen_ra_id`) REFERENCES `raum` (`ra_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `sensor_ibfk_2` FOREIGN KEY (`sen_havc_id`) REFERENCES `havc` (`havc_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor`
--

LOCK TABLES `sensor` WRITE;
/*!40000 ALTER TABLE `sensor` DISABLE KEYS */;
INSERT INTO `sensor` VALUES (1,'Tem & Feu 01','Tem & Feu','Klassenraum 001',1,1),(2,'Tem & Feu 02','Tem & Feu','Klassenraum 002',2,1),(3,'Tem & Feu 03','Tem & Feu','Klassenraum 003',3,1),(4,'Tem & Feu 04','Tem & Feu','Klassenraum 101',4,2),(5,'Tem & Feu 05','Tem & Feu','Klassenraum 102',5,2),(6,'Tem & Feu 06','Tem & Feu','Klassenraum 103',6,2),(7,'Tem & Feu 07','Tem & Feu','Kunst',7,3),(8,'Tem & Feu 08','Tem & Feu','Musik',8,3),(9,'Tem & Feu 09','Tem & Feu','Werk',9,3);
/*!40000 ALTER TABLE `sensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensordaten`
--

DROP TABLE IF EXISTS `sensordaten`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sensordaten` (
  `seda_id` int(11) NOT NULL AUTO_INCREMENT,
  `seda_zeit` datetime DEFAULT NULL,
  `seda_temperatur` double DEFAULT NULL,
  `seda_feuch` double DEFAULT NULL,
  `seda_sen_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`seda_id`),
  KEY `seda_sen_id` (`seda_sen_id`),
  CONSTRAINT `sensordaten_ibfk_1` FOREIGN KEY (`seda_sen_id`) REFERENCES `sensor` (`sen_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensordaten`
--

LOCK TABLES `sensordaten` WRITE;
/*!40000 ALTER TABLE `sensordaten` DISABLE KEYS */;
INSERT INTO `sensordaten` VALUES (1,'2017-07-26 00:38:14',35,50,1),(2,'2017-07-26 00:38:14',45,50,1);
/*!40000 ALTER TABLE `sensordaten` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockwerk`
--

DROP TABLE IF EXISTS `stockwerk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stockwerk` (
  `sw_id` int(11) NOT NULL AUTO_INCREMENT,
  `sw_bezeichnung` varchar(50) DEFAULT NULL,
  `sw_ifc_guid` int(11) DEFAULT NULL,
  `sw_ge_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sw_id`),
  KEY `sw_ge_id` (`sw_ge_id`),
  CONSTRAINT `stockwerk_ibfk_1` FOREIGN KEY (`sw_ge_id`) REFERENCES `gebaeude` (`ge_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockwerk`
--

LOCK TABLES `stockwerk` WRITE;
/*!40000 ALTER TABLE `stockwerk` DISABLE KEYS */;
INSERT INTO `stockwerk` VALUES (1,'Ebene 0',10,1),(2,'Ebene 1',11,1),(3,'Ebene 2',12,1);
/*!40000 ALTER TABLE `stockwerk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wand`
--

DROP TABLE IF EXISTS `wand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `wand` (
  `wa_id` int(11) NOT NULL AUTO_INCREMENT,
  `wa_schaden` varchar(50) DEFAULT NULL,
  `wa_ifc_guid` int(11) DEFAULT NULL,
  PRIMARY KEY (`wa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wand`
--

LOCK TABLES `wand` WRITE;
/*!40000 ALTER TABLE `wand` DISABLE KEYS */;
INSERT INTO `wand` VALUES (1,'Keiner Schaden',1011),(2,'Keiner Schaden',1012),(3,'Keiner Schaden',1013),(4,'Keiner Schaden',1014),(5,'Keiner Schaden',1025),(6,'Keiner Schaden',1026),(7,'Keiner Schaden',1027),(8,'Keiner Schaden',1038),(9,'Keiner Schaden',1039),(10,'Keiner Schaden',10310),(11,'Keiner Schaden',1111),(12,'Keiner Schaden',1112),(13,'Keiner Schaden',1113),(14,'Keiner Schaden',1114),(15,'Keiner Schaden',1125),(16,'Keiner Schaden',1126),(17,'Keiner Schaden',1127),(18,'Keiner Schaden',1138),(19,'Keiner Schaden',1139),(20,'Keiner Schaden',11310),(21,'Keiner Schaden',1211),(22,'Keiner Schaden',1212),(23,'Keiner Schaden',1213),(24,'Keiner Schaden',1214),(25,'Keiner Schaden',1225),(26,'Keiner Schaden',1226),(27,'Keiner Schaden',1227),(28,'Keiner Schaden',1238),(29,'Keiner Schaden',1239),(30,'Keiner Schaden',12310);
/*!40000 ALTER TABLE `wand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'iib2_hue1_gruppe6'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-02 20:49:52
