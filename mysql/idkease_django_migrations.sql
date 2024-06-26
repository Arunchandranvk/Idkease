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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-03 16:26:10.165694'),(2,'contenttypes','0002_remove_content_type_name','2024-04-03 16:49:01.986702'),(3,'auth','0001_initial','2024-04-03 16:49:02.351049'),(4,'auth','0002_alter_permission_name_max_length','2024-04-03 16:49:02.417368'),(5,'auth','0003_alter_user_email_max_length','2024-04-03 16:49:02.423012'),(6,'auth','0004_alter_user_username_opts','2024-04-03 16:49:02.429928'),(7,'auth','0005_alter_user_last_login_null','2024-04-03 16:49:02.434500'),(8,'auth','0006_require_contenttypes_0002','2024-04-03 16:49:02.439752'),(9,'auth','0007_alter_validators_add_error_messages','2024-04-03 16:49:02.449053'),(10,'auth','0008_alter_user_username_max_length','2024-04-03 16:49:02.460328'),(11,'auth','0009_alter_user_last_name_max_length','2024-04-03 16:49:02.469715'),(12,'auth','0010_alter_group_name_max_length','2024-04-03 16:49:02.490902'),(13,'auth','0011_update_proxy_permissions','2024-04-03 16:49:02.503395'),(14,'auth','0012_alter_user_first_name_max_length','2024-04-03 16:49:02.514597'),(15,'accounts','0001_initial','2024-04-03 16:49:02.955416'),(16,'accounts','0002_users_alter_custuser_role','2024-04-03 16:49:03.008604'),(17,'accounts','0003_alter_users_aadhar_alter_users_address_and_more','2024-04-03 16:49:03.191482'),(18,'accounts','0004_complaint','2024-04-03 16:49:03.207215'),(19,'accounts','0005_rename_local_body_complaint_localbody','2024-04-03 16:49:03.226526'),(20,'accounts','0006_alter_complaint_is_solved','2024-04-03 16:49:03.265482'),(21,'admin','0001_initial','2024-04-03 16:49:33.244014'),(22,'admin','0002_logentry_remove_auto_add','2024-04-03 16:49:33.244014'),(23,'admin','0003_logentry_add_action_flag_choices','2024-04-03 16:49:33.260571'),(24,'authtoken','0001_initial','2024-04-03 16:49:33.375233'),(25,'authtoken','0002_auto_20160226_1747','2024-04-03 16:49:33.405631'),(26,'authtoken','0003_tokenproxy','2024-04-03 16:49:33.411789'),(27,'authtoken','0004_alter_tokenproxy_options','2024-04-03 16:49:33.415393'),(28,'sessions','0001_initial','2024-04-03 16:49:33.447438'),(29,'accounts','0007_recommendation','2024-05-01 12:39:24.924699'),(30,'accounts','0008_remove_recommendation_audio_and_more','2024-05-01 13:24:48.358613'),(31,'accounts','0009_alter_complaint_authority_alter_complaint_member','2024-05-01 13:32:34.367101'),(32,'accounts','0002_alter_custuser_role','2024-05-01 14:41:53.503603'),(33,'accounts','0003_authority_alter_custuser_role','2024-05-01 14:51:33.082979'),(34,'accounts','0004_trackingrecom','2024-05-01 14:58:06.589011');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-01 20:33:19
