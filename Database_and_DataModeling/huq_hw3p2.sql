-- Date updated: 02/07/2022
-- BY: Miftahul Huq
-- Course: ISTE 230

-- Task 1
INSERT INTO contactInfo
(contactID, firstName, middleInitial, lastName, email, url, birthday, notes)
VALUES (3, 'Eli', 'T', 'Wallowby', 'etwallowby@concor.com', 'www.concor.com/~wallowby', '1956-03-26', 'All meetings must be scheduled through his assistant.'),
       (4, 'Eve', 'C', 'Sampson', 'esampson@concor.com', NULL, '1972-05-11', 'Very helpful.'),
	   (5, 'Carson', 'B', 'Campbell', 'cbc232@mvch.org', NULL, '1955-01-05', 'Wife: Lisa Kids: Lucas, Lucy, and Lucinda.');
	   
-- Task 2
ALTER TABLE contactInfo
ADD nickname VARCHAR(20) NULL DEFAULT 'To Be Determined';

-- Task 3
ALTER TABLE contactInfo
CHANGE firstName firstName VARCHAR(15) NOT NULL;

ALTER TABLE contactInfo
CHANGE lastName lastName VARCHAR(25) NOT NULL;

-- Task 4
UPDATE contactInfo
SET nickname = 'Dave'
WHERE firstName = 'David' AND lastName = 'Munson';

-- Task 5
DELETE
FROM contactInfo
WHERE url = 'www.concor.com/~wallowby';
	   