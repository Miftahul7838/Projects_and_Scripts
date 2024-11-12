-- Name: Miftahul Huq
-- Date: 04/12/2022
-- Course: ISTE-230

-- Using the jobsv2 DATABASE
USE jobsv2;

-- Question 1

SELECT stateCode
FROM Employer
UNION
SELECT location
FROM Quarter;

-- Question 2

SELECT Employer.companyName, Employer.division, Employer.stateCode, Interview.salaryOffered
FROM Employer INNER JOIN Interview
ON Employer.companyName = Interview.companyName AND Employer.division = Interview.division;

-- Question 3

SELECT stateCode, description
FROM state
WHERE stateCode NOT IN (
	SELECT stateCode
	FROM Employer
);

-- Question 4

SELECT DISTINCT companyName, minHrsOffered
FROM Interview;

-- Question 5

SELECT stateCode, description
FROM state 
WHERE description LIKE '__a%' OR description LIKE '__e%' OR description LIKE '__i%' OR
description LIKE '__o%' OR description LIKE '__u%';

-- Question 6

SELECT quarter.qtrCode, quarter.location, state.description
FROM quarter, state
WHERE quarter.location = state.stateCode;

-- Question 7

SELECT state.description, employer.companyName
FROM state LEFT JOIN employer
ON state.stateCode = employer.stateCode;