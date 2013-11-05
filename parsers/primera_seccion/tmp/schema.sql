CREATE TABLE `designaciones` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `persona_id` int(50) DEFAULT NULL,
  `dependencia_id` int(50) DEFAULT NULL,
  `puesto_id` int(50) DEFAULT NULL,
  `articulo_id` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `persona_id` (`persona_id`),
  KEY `dependencia_id` (`dependencia_id`),
  KEY `puesto_id` (`puesto_id`),
  KEY `puestos_id_index` (`id`),
  KEY `fk_articulos` (`articulo_id`),
  CONSTRAINT `designaciones_ibfk_1` FOREIGN KEY (`persona_id`) REFERENCES `personas` (`id`),
  CONSTRAINT `designaciones_ibfk_2` FOREIGN KEY (`dependencia_id`) REFERENCES `dependencias` (`id`),
  CONSTRAINT `designaciones_ibfk_3` FOREIGN KEY (`puesto_id`) REFERENCES `puestos` (`id`),
  CONSTRAINT `designaciones_ibfk_4` FOREIGN KEY (`articulo_id`) REFERENCES `articulos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE `puestos` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nombre` text,
  PRIMARY KEY (`id`),
  KEY `puestos_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE `dependencias` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nombre` text,
  PRIMARY KEY (`id`),
  KEY `puestos_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

 CREATE TABLE `personas` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `codigo_tipo` varchar(10) DEFAULT NULL,
  `codigo_numero` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `puestos_id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE `articulos` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `texto` text,
  PRIMARY KEY (`id`),
  KEY `id_index` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

