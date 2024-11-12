-- Name: Miftahul Huq
-- Date: 05/02/2022
-- Course: ISTE-230 (Final Practical)

-- Using the jobsv2 database
USE jobsv2;

-- Question 1 (From Tables: Employer, State, Interview)

/** SELECT Employer.companyName AS "COMPANY", Employer.division AS "DIVISION", CONCAT(city, ', ', description) AS "LOCATION"
FROM Employer, State, Interview
WHERE Employer.companyName = Interview.companyName AND Employer.division = Interview.division 
GROUP BY **/

-- Question 2

SELECT stateCode AS "statecode"
FROM Employer LEFT JOIN Quarter
ON Employer.stateCode IN (
    SELECT stateCode
    FROM quarter
); 

-- Question 4
SELECT companyName AS "Company Name", Interview.qtrcode AS "Term", COUNT(Interview.qtrcode) AS "Number of Interviews Offered", MAX(salaryOffered)
FROM Interview JOIN Quarter
ON Interview.qtrcode = Quarter.qtrcode
WHERE Interview.salaryOffered >= Quarter.minsal
GROUP BY companyName, Interview.qtrcode
HAVING COUNT(Interview.qtrcode) >= 2;

-- Question 3
SELECT DISTINCT Employer.companyName AS "Company Name", interviewDate AS "Interview Date"
FROM Employer LEFT JOIN Interview
ON Employer.companyName = Interview.companyName
WHERE Employer.companyName LIKE '__me%' OR Employer.companyName LIKE '__ch%'
ORDER BY Employer.companyName DESC, interviewDate DESC;

-- Question 5
START TRANSACTION;
    INSERT INTO quarter
    (qtrcode, location, minsal, minhrs)
    VALUES ('20131', 'NY', 30.00, 30),
           ('20132', 'CA', 60.00, 60);
COMMIT;

-- Question 6
CREATE TABLE Travel (
    travelID INT UNSIGNED AUTO_INCREMENT,
    interviewID INT UNSIGNED,
    DepartLoc CHAR(5) NOT NULL,
    destinationDate DATE NOT NULL,
    destinationLoc CHAR(5) NOT NULL,
    bookingAgen VARCHAR(75),
    paid ENUM('y','n') NOT NULL,
    CONSTRAINT PRIMARY KEY(travelID,interviewID),
    CONSTRAINT InterviewTravel_fk FOREIGN KEY(interviewID) REFERENCES Interview(interviewID) 
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
