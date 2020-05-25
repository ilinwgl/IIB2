-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: demonstrator
-- ------------------------------------------------------
-- Server version	5.7.26-log

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
-- Table structure for table `bauleiter`
--
CREATE DATABASE demonstrator;
USE demonstrator;
DROP TABLE IF EXISTS `bauleiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bauleiter` (
  `blt_id` int(11) NOT NULL AUTO_INCREMENT,
  `blt_name` varchar(50) DEFAULT NULL,
  `blt_vorname` varchar(50) DEFAULT NULL,
  `blt_username` varchar(50) DEFAULT NULL,
  `blt_passwort` blob,
  PRIMARY KEY (`blt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bauleiter`
--

LOCK TABLES `bauleiter` WRITE;
/*!40000 ALTER TABLE `bauleiter` DISABLE KEYS */;
INSERT INTO `bauleiter` VALUES (1,'Burch','Timmy','Timmy!',_binary 'Timmy!'),(2,'Fritz','J√∂rg','jf',_binary '\r\√¡–óÇı@Eë\Ô\ÂcîZwM'),(3,'Rieger','Bastian',NULL,NULL),(7,'Bach','Johann','JSBach',NULL),(8,'Bach','Johann','JSBach',NULL),(9,'Bach','Johann','JSBach',NULL);
/*!40000 ALTER TABLE `bauleiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gebaeude`
--

DROP TABLE IF EXISTS `gebaeude`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `gebaeude` (
  `geb_id` int(11) NOT NULL AUTO_INCREMENT,
  `geb_plz` int(6) unsigned DEFAULT NULL,
  `geb_strasse` varchar(50) DEFAULT NULL,
  `geb_hausnummer` varchar(4) DEFAULT NULL,
  `geb_guid` varchar(50) DEFAULT NULL,
  `geb_blt_id` int(11) DEFAULT NULL,
  `geb_ort` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`geb_id`),
  KEY `geb_b_id` (`geb_blt_id`),
  CONSTRAINT `geb_b_id` FOREIGN KEY (`geb_blt_id`) REFERENCES `bauleiter` (`blt_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gebaeude`
--

LOCK TABLES `gebaeude` WRITE;
/*!40000 ALTER TABLE `gebaeude` DISABLE KEYS */;
INSERT INTO `gebaeude` VALUES (1,60386,'Am Erlenbruch','22',NULL,1,'Frankfurt'),(2,60314,'Hanauer Landstra√üe','137',NULL,2,'Frankfurt'),(3,64287,'Franziska-Braun-Str','7',NULL,3,'Darmstadt'),(4,60386,'Carl-Brenz-Stra√üe','37',NULL,3,'Frankfurt'),(5,60320,'Eichendorffstra√üe','13',NULL,1,'Frankfurt'),(6,64287,'Franziska-Braun-Str','5',NULL,2,'Darmstadt'),(7,64287,'Franziska-Braun-Str','3',NULL,1,'Darmstadt'),(8,60314,'Hanauer Landstra√üe','133',NULL,3,'Frankfurt');
/*!40000 ALTER TABLE `gebaeude` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gutachten`
--

DROP TABLE IF EXISTS `gutachten`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `gutachten` (
  `gut_id` int(11) NOT NULL AUTO_INCREMENT,
  `gut_datum` date DEFAULT NULL,
  `gut_mangel` varchar(50) DEFAULT NULL,
  `gut_beschreibung` varchar(50) DEFAULT NULL,
  `gut_wan_id` int(11) DEFAULT NULL,
  `gut_gar_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`gut_id`),
  KEY `FK_Gutachten_wand` (`gut_wan_id`),
  KEY `FK_Gutachten_gutachter` (`gut_gar_id`),
  CONSTRAINT `FK_Gutachten_gutachter` FOREIGN KEY (`gut_gar_id`) REFERENCES `gutachter` (`gar_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `FK_Gutachten_wand` FOREIGN KEY (`gut_wan_id`) REFERENCES `wand` (`wan_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gutachten`
--

LOCK TABLES `gutachten` WRITE;
/*!40000 ALTER TABLE `gutachten` DISABLE KEYS */;
INSERT INTO `gutachten` VALUES (1,'2017-04-16','Riss','10 mm',1,2),(2,'2017-04-16','Schimmel','30 cm¬≤',12,NULL),(3,'2017-04-16','Riss','12 mm',13,NULL),(4,'2017-04-16','Putz br√∂ckelt','rechts oben',14,3),(5,'2017-04-16','Schimmel','10 cm¬≤',15,3),(6,'2017-04-16','Fuge l√∂st sich','20 cm',16,2),(7,'2017-04-16','Feuchtigkeit','unten',17,3),(8,'2017-04-16','Algenbefall','1 m¬≤',18,2),(9,'2017-04-16','Riss','15 mm',19,NULL),(10,'2017-04-16','Putz br√∂ckelt','√ºberall',11,2),(11,'2017-04-16','Schimmel','hinter Schrank',10,NULL),(12,'2017-04-16','Feuchtigkeit','von oben',2,2),(13,'2017-04-16','Schimmel','an Fensteraussparung',3,2),(14,'2017-04-16','Putz br√∂ckelt','an Heizungsinstallation',4,3),(15,'2017-04-16','Riss','5 mm',5,2),(16,'2017-04-16','unsachgem√§√üe Installation von Rohren','D√§mmung defekt',6,3),(17,'2017-04-16','Algenbefall','√ºber Fenster',7,3),(18,'2017-04-16','Loch','Wanddurchbruch durch Unfall',8,2),(19,'2017-04-16','Schiefe Wand','fehlerhafte Erstellung Mauerwerk',9,NULL),(20,'2017-04-16','Wand kippt nach innen','Beeintr√§chtigung Tragf√§higkeit',20,2);
/*!40000 ALTER TABLE `gutachten` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gutachter`
--

DROP TABLE IF EXISTS `gutachter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `gutachter` (
  `gar_id` int(11) NOT NULL AUTO_INCREMENT,
  `gar_name` varchar(50) DEFAULT NULL,
  `gar_vorname` varchar(50) DEFAULT NULL,
  `gar_username` varchar(50) DEFAULT NULL,
  `gar_passwort` blob,
  PRIMARY KEY (`gar_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gutachter`
--

LOCK TABLES `gutachter` WRITE;
/*!40000 ALTER TABLE `gutachter` DISABLE KEYS */;
INSERT INTO `gutachter` VALUES (2,'B√∂hler','Maria','m_boe',_binary 'ò‹≤q}\⁄\·R’≥Y\∆\Íó\‰˛4¢ùL'),(3,'Feldhase','Frieda','zucker',_binary 'sÔøΩÔøΩ'),(4,'Schmidt','Karl',NULL,NULL),(5,'Vogel','Nina','Kuecken',_binary 'pieps!');
/*!40000 ALTER TABLE `gutachter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lnraumwand`
--

DROP TABLE IF EXISTS `lnraumwand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lnraumwand` (
  `lrw_id` int(11) NOT NULL AUTO_INCREMENT,
  `lrw_rau_id` int(11) DEFAULT NULL,
  `lrw_wan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`lrw_id`),
  KEY `r_id` (`lrw_rau_id`),
  KEY `w_id` (`lrw_wan_id`),
  CONSTRAINT `r_id` FOREIGN KEY (`lrw_rau_id`) REFERENCES `raum` (`rau_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `w_id` FOREIGN KEY (`lrw_wan_id`) REFERENCES `wand` (`wan_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lnraumwand`
--

LOCK TABLES `lnraumwand` WRITE;
/*!40000 ALTER TABLE `lnraumwand` DISABLE KEYS */;
INSERT INTO `lnraumwand` VALUES (1,1,1),(2,9,12),(3,8,13),(4,7,14),(5,6,15),(6,5,16),(7,4,17),(8,3,18),(9,2,19),(10,10,11),(11,11,10),(12,12,2),(13,13,3),(14,14,4),(15,15,5),(16,16,6),(17,17,7),(18,18,8),(19,19,9),(20,20,20);
/*!40000 ALTER TABLE `lnraumwand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `multiusingbesp`
--

DROP TABLE IF EXISTS `multiusingbesp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `multiusingbesp` (
  `ID` int(11) NOT NULL,
  `Vorname` varchar(45) DEFAULT NULL,
  `Timestamp_vorname` datetime DEFAULT NULL,
  `Nachname` varchar(45) DEFAULT NULL,
  `Timestamp_nachname` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `multiusingbesp`
--

LOCK TABLES `multiusingbesp` WRITE;
/*!40000 ALTER TABLE `multiusingbesp` DISABLE KEYS */;
INSERT INTO `multiusingbesp` VALUES (1,'tata1','2019-05-09 11:39:33','shi','2019-05-09 11:25:31'),(2,'Johann','2019-05-09 11:25:05','schmitt','2019-05-09 11:25:28'),(3,'Anna','2019-05-09 11:25:13','wagner','2019-05-09 11:25:24');
/*!40000 ALTER TABLE `multiusingbesp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raum`
--

DROP TABLE IF EXISTS `raum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `raum` (
  `rau_id` int(11) NOT NULL AUTO_INCREMENT,
  `rau_nummer` varchar(5) DEFAULT NULL,
  `rau_bezeichnung` varchar(50) DEFAULT NULL,
  `rau_guid` varchar(50) DEFAULT NULL,
  `rau_stw_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`rau_id`),
  KEY `r_s_id` (`rau_stw_id`),
  CONSTRAINT `r_s_id` FOREIGN KEY (`rau_stw_id`) REFERENCES `stockwerk` (`stw_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raum`
--

LOCK TABLES `raum` WRITE;
/*!40000 ALTER TABLE `raum` DISABLE KEYS */;
INSERT INTO `raum` VALUES (1,'1','Raum',NULL,11),(2,'1','Raum',NULL,138),(3,'1','Raum',NULL,30),(4,'1','Raum',NULL,74),(5,'1','Raum',NULL,52),(6,'1','Raum',NULL,41),(7,'1','Raum',NULL,19),(8,'1','Raum',NULL,63),(9,'1','Raum',NULL,44),(10,'1','Raum',NULL,15),(11,'1','Raum',NULL,57),(12,'1','Raum',NULL,71),(13,'1','Raum',NULL,51),(14,'1','Raum',NULL,18),(15,'1','Raum',NULL,38),(16,'1','Raum',NULL,60),(17,'1','Raum',NULL,26),(18,'1','Raum',NULL,141),(19,'1','Raum',NULL,49),(20,'1','Raum',NULL,36);
/*!40000 ALTER TABLE `raum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stockwerk`
--

DROP TABLE IF EXISTS `stockwerk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `stockwerk` (
  `stw_id` int(11) NOT NULL AUTO_INCREMENT,
  `stw_bezeichnung` varchar(50) DEFAULT NULL,
  `stw_guid` varchar(50) DEFAULT NULL,
  `stw_geb_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`stw_id`),
  KEY `s_geb_id` (`stw_geb_id`),
  CONSTRAINT `s_geb_id` FOREIGN KEY (`stw_geb_id`) REFERENCES `gebaeude` (`geb_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=146 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stockwerk`
--

LOCK TABLES `stockwerk` WRITE;
/*!40000 ALTER TABLE `stockwerk` DISABLE KEYS */;
INSERT INTO `stockwerk` VALUES (11,'EG','',2),(12,'OG_1','',2),(13,'OG_2','',2),(14,'OG_3','',2),(15,'OG_4','',2),(16,'OG_5','',2),(17,'OG_6','',2),(18,'OG_7','',2),(19,'EG','',3),(20,'OG_8','',3),(21,'OG_9','',3),(22,'OG_10','',3),(23,'OG_1','',3),(24,'OG_2','',3),(25,'OG_3','',3),(26,'OG_4','',3),(27,'OG_5','',3),(28,'OG_6','',3),(29,'OG_7','',3),(30,'EG','',4),(31,'OG_8','',4),(32,'OG_9','',4),(33,'OG_10','',4),(34,'OG_1','',4),(35,'OG_2','',4),(36,'OG_3','',4),(37,'OG_4','',4),(38,'OG_5','',4),(39,'OG_6','',4),(40,'OG_7','',4),(41,'EG','',5),(42,'OG_8','',5),(43,'OG_9','',5),(44,'OG_10','',5),(45,'OG_1','',5),(46,'OG_2','',5),(47,'OG_3','',5),(48,'OG_4','',5),(49,'OG_5','',5),(50,'OG_6','',5),(51,'OG_7','',5),(52,'EG','',6),(53,'OG_8','',6),(54,'OG_9','',6),(55,'OG_10','',6),(56,'OG_1','',6),(57,'OG_2','',6),(58,'OG_3','',6),(59,'OG_4','',6),(60,'OG_5','',6),(61,'OG_6','',6),(62,'OG_7','',6),(63,'EG','',7),(64,'OG_8','',7),(65,'OG_9','',7),(66,'OG_10','',7),(67,'OG_1','',7),(68,'OG_2','',7),(69,'OG_3','',7),(70,'OG_4','',7),(71,'OG_5','',7),(72,'OG_6','',7),(73,'OG_7','',7),(74,'EG','',8),(75,'UG_1','',8),(76,'UG_2','',8),(77,'UG_3','',8),(78,'UG_4','',8),(79,'UG_5','',8),(80,'UG_6','',8),(81,'UG_7','',8),(82,'UG_8','',8),(138,'EG',NULL,1),(139,'OG_1',NULL,1),(140,'OG_2',NULL,1),(141,'OG_3',NULL,1),(142,'OG_8',NULL,1),(143,'UG_2',NULL,1),(144,'UG_1',NULL,1),(145,'UG_3',NULL,1);
/*!40000 ALTER TABLE `stockwerk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wand`
--

DROP TABLE IF EXISTS `wand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `wand` (
  `wan_id` int(11) NOT NULL AUTO_INCREMENT,
  `wan_guid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`wan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wand`
--

LOCK TABLES `wand` WRITE;
/*!40000 ALTER TABLE `wand` DISABLE KEYS */;
INSERT INTO `wand` VALUES (1,'1'),(2,'12'),(3,'13'),(4,'14'),(5,'15'),(6,'16'),(7,'17'),(8,'18'),(9,'19'),(10,'11'),(11,'10'),(12,'2'),(13,'3'),(14,'4'),(15,'5'),(16,'6'),(17,'7'),(18,'8'),(19,'9'),(20,'20');
/*!40000 ALTER TABLE `wand` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-09 19:14:32
