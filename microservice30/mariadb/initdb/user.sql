SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `userdata30` (
  `id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `userdata30`
  ADD PRIMARY KEY (`id`);
  
ALTER TABLE `userdata30`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
