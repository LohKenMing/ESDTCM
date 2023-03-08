DROP SCHEMA IF EXISTS prescription;
CREATE SCHEMA prescription;
USE prescription;

DROP TABLE IF EXISTS `prescriptions`;
CREATE TABLE `department` (
  `Date` date DEFAULT NULL,
  `OrderID` int NOT NULL,  
  `Price` int DEFAULT NULL,
  `Status` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`OrderID`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `department` WRITE;
INSERT INTO `department` VALUES ('2015-03-20', 123, 100, 'Make Payment')
UNLOCK TABLES;