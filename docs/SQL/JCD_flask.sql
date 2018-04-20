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
CREATE TABLE `JCD_flask` (
  `number` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `contract_name` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `bike_stands` varchar(45) DEFAULT NULL,
  `available_bike_stands` varchar(45) DEFAULT NULL,
  `available_bikes` varchar(45) DEFAULT NULL,
  `last_update` timestamp NULL DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `OYB_timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lat` float DEFAULT NULL,
  `lng` float DEFAULT NULL,
  `banking` tinyint(4) DEFAULT NULL,
  `bonus` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
