要求三
1.
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
![image](https://user-images.githubusercontent.com/93469479/151373504-39cb7f45-a2fb-4b08-89ee-22d1ec2b529e.png)

2.
SELECT * FROM `member`; 
![image](https://user-images.githubusercontent.com/93469479/151373748-3f0f1d31-ce31-4c60-9579-8609426d9902.png)

3.
SELECT * FROM `member`ORDER BY `time` ASC;
![image](https://user-images.githubusercontent.com/93469479/151373846-4c28d104-fec4-4d41-8ef9-7ad867d44b29.png)

4.
SELECT * FROM `member`
ORDER BY `time` ASC
LIMIT 1,3;
![image](https://user-images.githubusercontent.com/93469479/151373957-4ef5c695-f79e-4e0d-be42-627069f4b6fb.png)

5.
SELECT * FROM `member` WHERE `username`='test';
![image](https://user-images.githubusercontent.com/93469479/151374049-e3af28e5-2032-4921-855c-55a02a54dc3e.png)

6.
SELECT * FROM `member` WHERE `username`='test' AND `password`='test';
![image](https://user-images.githubusercontent.com/93469479/151374136-d9e823a9-5c58-4275-a0fa-8925550baf3d.png)

7.
SET SQL_SAFE_UPDATES=0;
UPDATE `member` SET `name`='test2' WHERE `username`='test';
![image](https://user-images.githubusercontent.com/93469479/151374271-c9776306-5cc1-4f18-b0c4-5005850ec51f.png)

要求四
1.
SELECT COUNT(`id`) FROM `member`;
![image](https://user-images.githubusercontent.com/93469479/151374547-8398ee0d-227b-49da-8a6d-2a321aefc7b8.png)

2.
SELECT SUM(`follower_count`) FROM `member`;
![image](https://user-images.githubusercontent.com/93469479/151374661-c5f3d38f-ae96-4d91-bda9-024219ab7e45.png)

3.
SELECT AVG(`follower_count`) FROM `member`;
![image](https://user-images.githubusercontent.com/93469479/151374730-eac9b43c-3f6b-4f9e-956f-3760a8743473.png)

要求五
1.
SELECT `member`.`id`,`member`.`name`,`message`.`content`
FROM `member`
JOIN `message`
ON `member`.`id`= `message`.`member_id`;
![image](https://user-images.githubusercontent.com/93469479/151375322-174d0874-eaac-4557-87ca-46c07a0c409c.png)

2.
SELECT `member`.`id`,`member`.`name`,`message`.`content`
FROM `member`
JOIN `message`
ON `member`.`id`= `message`.`member_id` AND `member`.`username`='test';
![image](https://user-images.githubusercontent.com/93469479/151375424-47a960e2-37d7-4f58-bc16-1bb6b65ae139.png)







