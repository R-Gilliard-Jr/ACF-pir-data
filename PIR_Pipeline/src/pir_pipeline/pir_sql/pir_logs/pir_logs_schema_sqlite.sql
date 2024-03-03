CREATE TABLE `pir_ingestion_logs` (
    `run` TIMESTAMP,
    `timestamp` TIMESTAMP,
    `message` TEXT,
    PRIMARY KEY (`run`, `timestamp`)
);

CREATE TABLE `pir_question_linkage_logs` (
    `run` TIMESTAMP,
    `timestamp` TIMESTAMP,
    `message` TEXT,
    PRIMARY KEY (`run`, `timestamp`)
);

CREATE TABLE `mysql_logs` (
    `timestamp` TIMESTAMP,
    `message` TEXT
);

CREATE TABLE `security_logs` (
    `timestamp` TIMESTAMP,
    `message` TEXT
);

CREATE TABLE `pir_listener_logs` (
    `run` TIMESTAMP,
    `timestamp` TIMESTAMP,
    `message` TEXT,
    PRIMARY KEY (`run`, `timestamp`)
);

CREATE TABLE `pir_manual_question_link` (
    `timestamp` TIMESTAMP,
    `base_id` TEXT,
    `linked_id` TEXT,
    `type` TEXT
);