-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: idkease
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_complaint`
--

DROP TABLE IF EXISTS `accounts_complaint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `localbody` varchar(100) NOT NULL,
  `ward` varchar(100) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `is_solved` tinyint(1) NOT NULL,
  `authority` varchar(100) DEFAULT NULL,
  `member` varchar(100) DEFAULT NULL,
  `user_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_complaint_user_id_01b4be71_fk_accounts_custuser_id` (`user_id`),
  CONSTRAINT `accounts_complaint_user_id_01b4be71_fk_accounts_custuser_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_custuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_complaint`
--

LOCK TABLES `accounts_complaint` WRITE;
/*!40000 ALTER TABLE `accounts_complaint` DISABLE KEYS */;
INSERT INTO `accounts_complaint` VALUES (1,'Chorod','5','KSEB','Light is not working',0,'Accept','Reject',NULL),(2,'Vadakara','10','Water Authority','Water very bad',0,'Reject','Reject',NULL),(3,'kochi','5','KSEB','Powercut',0,'Not Available','Accept',NULL),(4,'kochi','5','KSEB','Powercut',0,'Not Available','Accept',NULL);
/*!40000 ALTER TABLE `accounts_complaint` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-01 20:33:17
