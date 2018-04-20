CREATE TABLE `JCD_dynamic_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  `bike_stands` varchar(45) DEFAULT NULL,
  `available_bike_stands` varchar(45) DEFAULT NULL,
  `available_bikes` varchar(45) DEFAULT NULL,
  `last_update` timestamp NULL DEFAULT NULL,
  `OYB_timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4889 DEFAULT CHARSET=utf8;
