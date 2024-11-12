-- Name: Miftahul Huq
-- Date: 02/23/2022

-- Part 1, question 1
CREATE DATABASE huqMP;

-- Part 1, question 2
USE huqMP;

-- Part 1, questoin 3
CREATE TABLE Coupon (

    CouponID INT UNIQUE,
    BrandName VARCHAR(50) NOT NULL,
    ProductName VARCHAR(75) NOT NULL,
    Discount float(4,2) NOT NULL DEFAULT (10.00),
    ExpDate Date NULL,
    Type CHAR(2) NULL,
    CONSTRAINT CouponID_pk PRIMARY KEY(CouponID)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Part 1, question 4
ALTER TABLE Coupon
ADD MaxCopies INT NOT NULL DEFAULT 1;

-- Part 1, question 5
DESC Coupon;

-- Part 1, question 6
INSERT INTO Coupon
(CouponID, BrandName, ProductName, ExpDate)
VALUE(1, 'Mainstays', '2 Slice Black Toaster', '2020-11-27');

-- Part 1, question 7
DELETE 
FROM Coupon
WHERE ExpDate < '2020-12-25';

-- ######################################### GOING INTO PART 2 ################################

-- Extra step
USE co_op;

-- Part 2, question 8
SELECT interviewID
FROM interview
WHERE qtrcode IS NULL;

-- Part 2, question 9
UPDATE Coupon
SET division = 'R and D'
WHERE division = 'RandD';

-- Part 2, question 10
SELECT companyname, salaryoffered
FROM interview
WHERE division = 'Development' AND (salaryoffered = 12.25 OR salaryoffered > 12.25);

-- Part 2, question 11
SELECT interviewdate, companyname
FROM interview
WHERE interviewdate LIKE '____-06-__';

-- Part 2, question 12
DROP TABLE interview;