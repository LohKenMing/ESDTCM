DROP SCHEMA IF EXISTS prescription;
CREATE SCHEMA prescription;
USE prescription;

DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `PatientID` int NOT NULL,
  `Name` varchar(90) DEFAULT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Drug ID` int DEFAULT NULL,
  `Drug Name` varchar(90) DEFAULT NULL,
  `Status` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`PatientID`),
--   KEY `Dept_fk` (`ParentDept`),
--   CONSTRAINT `Dept_fk` FOREIGN KEY (`ParentDept`) REFERENCES `department` (`DeptID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;