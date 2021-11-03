DROP DATABASE IF EXISTS bascula;
CREATE DATABASE bascula;
USE bascula;

CREATE TABLE IF NOT EXISTS `bascula`.`auth_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`django_content_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`auth_permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC) VISIBLE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `bascula`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`auth_group_permissions` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `bascula`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `bascula`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(150) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`auth_user_groups` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC) VISIBLE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `bascula`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `bascula`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`auth_user_user_permissions` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `bascula`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `bascula`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`django_admin_log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC) VISIBLE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `bascula`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `bascula`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`django_migrations` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `bascula`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE TRANSPORTISTAS(
    ID BIGINT UNSIGNED AUTO_INCREMENT,
    CODIGO INT UNSIGNED NOT NULL, 
    NOMBRE VARCHAR(255) NOT NULL,
    NOMBRE_FANTASIA VARCHAR(255) NOT NULL,
    CUIT VARCHAR(13) NOT NULL,
    FCREACION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO BOOLEAN DEFAULT 1,
    CONSTRAINT PK_TRANSPORTISTAS PRIMARY KEY (ID, CODIGO),
    CONSTRAINT UNQ_TRANSPORTISTAS_CODIGO UNIQUE (CODIGO),
    CONSTRAINT UNQ_TRANSPORTISTAS_CUIT UNIQUE (CUIT)
);

CREATE TABLE CAMIONES(
    ID BIGINT UNSIGNED AUTO_INCREMENT,
    PATENTE VARCHAR(7) NOT NULL,
    CODIGO_TRANSPORTISTA INT UNSIGNED NOT NULL,
    TARA FLOAT NOT NULL, 
    FCREACION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO BOOLEAN DEFAULT 1,
    CONSTRAINT PK_CAMIONES PRIMARY KEY (ID),
    CONSTRAINT FK_CAMIONES_TRANSPORTISTAS FOREIGN KEY (CODIGO_TRANSPORTISTA) REFERENCES TRANSPORTISTAS(CODIGO),
    CONSTRAINT UNQ_CAMIONES_PATENTE UNIQUE (PATENTE)
);

CREATE TABLE DESTINOS(
    ID BIGINT UNSIGNED AUTO_INCREMENT,
    NOMBRE VARCHAR(255) NOT NULL,
    FCREACION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO BOOLEAN DEFAULT 1,
    CONSTRAINT PK_DESTINOS PRIMARY KEY (ID),
    CONSTRAINT UNQ_DESTINOS_NOMBRE UNIQUE (NOMBRE)
);

CREATE TABLE GENERADORES(
    ID BIGINT UNSIGNED AUTO_INCREMENT,
    NOMBRE VARCHAR(255) NOT NULL,
    NOMBRE_FANTASIA VARCHAR(255) NOT NULL,
    CUIT VARCHAR(13) NOT NULL,
    FCREACION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO BOOLEAN DEFAULT 1,
    CONSTRAINT PK_GENERADORES PRIMARY KEY (ID),
    CONSTRAINT UNQ_GENERADORES_CUIT UNIQUE (CUIT)
);

CREATE TABLE RESIDUOS(
    ID BIGINT UNSIGNED AUTO_INCREMENT,
    NOMBRE VARCHAR(255) NOT NULL,
    COSTO_TONELADA FLOAT NOT NULL,
    FCREACION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO BOOLEAN DEFAULT 1,
    CONSTRAINT PK_RESIDUOS PRIMARY KEY (ID),
    CONSTRAINT UNQ_RESIDUOS_NOMBRE UNIQUE (NOMBRE)
);

CREATE TABLE GENERADORES_RESIDUOS(
    ID BIGINT UNSIGNED AUTO_INCREMENT,
    ID_GENERADOR BIGINT UNSIGNED NOT NULL,
    ID_RESIDUO BIGINT UNSIGNED NOT NULL,
    FCREACION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO BOOLEAN DEFAULT 1,
    CONSTRAINT PK_GENERADORES_RESIDUOS PRIMARY KEY (ID),
    CONSTRAINT FK_GENRES_ID_GENERADOR FOREIGN KEY (ID_GENERADOR) REFERENCES GENERADORES(ID),
    CONSTRAINT FK_GENRES_ID_RESIDUO FOREIGN KEY (ID_RESIDUO) REFERENCES RESIDUOS(ID)
);

CREATE TABLE PESAJES(
    ID BIGINT UNSIGNED AUTO_INCREMENT,
    GENERADOR VARCHAR(255) NOT NULL,
    RESIDUO VARCHAR(255) NOT NULL,
    TRANSPORTISTA VARCHAR(255) NOT NULL,
    CAMION VARCHAR(255) NOT NULL,
    DESTINO VARCHAR(255) NOT NULL,
    PESAJE FLOAT NOT NULL,
    COSTO FLOAT NOT NULL,
    ID_USUARIO INT NOT NULL,
    FCREACION DATETIME DEFAULT CURRENT_TIMESTAMP,
    ACTIVO BOOLEAN DEFAULT 1,
    CONSTRAINT PK_PESAJES PRIMARY KEY (ID),
    CONSTRAINT FK_PESAJES_ID_USUARIO FOREIGN KEY (ID_USUARIO) REFERENCES AUTH_USER(ID)
);