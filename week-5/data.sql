CREATE DATABASE `website`;
SHOW DATABASES;

USE `website`;
CREATE TABLE `member`(
	`id` BIGINT PRIMARY KEY AUTO_INCREMENT, 
    `name` VARCHAR(255) NOT NULL,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `follower_count` INT NOT NULL DEFAULT '0',
    `time` DATETIME DEFAULT NOW()
);

SELECT * FROM `member`; #選取全部
DROP TABLE `member`; #刪除表格

INSERT INTO `member`(`id`,`name`,`username`,`password`,`follower_count`) 
VALUES(138,'APPLE','test','test',58);
INSERT INTO `member`(`id`,`name`,`username`,`password`,`follower_count`) 
VALUES(456,'BANANA','banana','banana',78);
INSERT INTO `member`(`id`,`name`,`username`,`password`,`follower_count`) 
VALUES(425,'ORANGE','orange','orange',46);
INSERT INTO `member`(`id`,`name`,`username`,`password`,`follower_count`) 
VALUES(016,'STRAWBERRY','strawberry','strawberry',89);
INSERT INTO `member`(`id`,`name`,`username`,`password`,`follower_count`) 
VALUES(765,'GUAVA','guava','guava',17);

SELECT * FROM `member`ORDER BY `time` ASC;
SELECT * FROM `member`
ORDER BY `time` ASC
LIMIT 1,3; #選取第2~4筆資料
SELECT * FROM `member` WHERE `username`='test';
SELECT * FROM `member` WHERE `username`='test' AND `password`='test';
SET SQL_SAFE_UPDATES=0;
UPDATE `member` SET `name`='test2' WHERE `username`='test';

SELECT COUNT(`id`) FROM `member`;
SELECT SUM(`follower_count`) FROM `member`;
SELECT AVG(`follower_count`) FROM `member`;

SELECT * FROM `message`; #選取全部
CREATE TABLE `message`(
	`id` BIGINT PRIMARY KEY AUTO_INCREMENT, 
    `member_id` BIGINT NOT NULL,
    `content` VARCHAR(255) NOT NULL,
    `time` DATETIME DEFAULT NOW(),
    FOREIGN KEY (`member_id`) REFERENCES `member`(`id`)
);

INSERT INTO `message` (`id`,`member_id`,`content`)
VALUES (202,'16','我是一顆草莓');
INSERT INTO `message` (`id`,`member_id`,`content`)
VALUES (208,'138','我是一顆蘋果');
INSERT INTO `message` (`id`,`member_id`,`content`)
VALUES (209,'138','我是一顆好吃的蘋果');
INSERT INTO `message` (`id`,`member_id`,`content`)
VALUES (220,'765','我是一顆巴辣');

SELECT `member`.`id`,`member`.`name`,`message`.`content`
FROM `member`
JOIN `message`
ON `member`.`id`= `message`.`member_id`;

SELECT `member`.`id`,`member`.`name`,`message`.`content`
FROM `member`
JOIN `message`
ON `member`.`id`= `message`.`member_id` AND `member`.`username`='test';


