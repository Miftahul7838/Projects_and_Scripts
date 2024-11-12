-- Name: Miftahul Huq
-- Updated: 04/07/2022
-- ISTS-230: Miftahul_Huq_HW7

-- CREATING THE DATABASE: ACMEOnline

DROP DATABASE IF EXISTS ACMEOnline;
CREATE DATABASE ACMEOnline;
SHOW DATABASES;
USE ACMEOnline;

-- CREATING TABLES: ACMEOnline relations:

CREATE TABLE Category (
	categoryName VARCHAR(35),
	shippingPerPound FLOAT(4,2),
	offersAllowed ENUM ('y', 'n'),
	CONSTRAINT categoryName_pk PRIMARY KEY(categoryName)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Item (
    itemNumber INT UNSIGNED AUTO_INCREMENT,
    itemName VARCHAR(35) NOT NULL,
    description VARCHAR(255),
    model VARCHAR(50) NOT NULL,
    price FLOAT(6,2) NOT NULL,
    categoryName VARCHAR(35),
    CONSTRAINT Item_pk PRIMARY KEY(itemNumber),
    CONSTRAINT CategoryItem_fk FOREIGN KEY(categoryName) REFERENCES Category(categoryName) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Offer (
    offerCode VARCHAR(15),
    discountAmt VARCHAR(35) NOT NULL,
    minAmount FLOAT(4,2) NOT NULL,
    expirationDate DATE NOT NULL,
    CONSTRAINT offer_pk PRIMARY KEY(offerCode)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Customer (
    customerID INT UNSIGNED AUTO_INCREMENT,
    customerName VARCHAR(50) NOT NULL,
    address VARCHAR(150) NOT NULL,
    email VARCHAR(80),
	customerType ENUM ('Home', 'Business'),
    CONSTRAINT customer_pk PRIMARY KEY(customerID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Business (
    customerID INT UNSIGNED,
    paymentTerms VARCHAR(50) NOT NULL,
    CONSTRAINT business_pk PRIMARY KEY(customerID),
    CONSTRAINT CustomerBUsiness_fk FOREIGN KEY(customerID) REFERENCES Customer(customerID) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Home (
    customerID INT UNSIGNED,
    creditCardNum CHAR(16) NOT NULL,
    cardExpirationDate CHAR(6) NOT NULL,
    CONSTRAINT home_pk PRIMARY KEY(customerID), 
    CONSTRAINT CustomerHome_fk FOREIGN KEY(customerID) REFERENCES Customer(customerID) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Ordered (
    orderID INT UNSIGNED AUTO_INCREMENT,
    totalCost FLOAT(8,2), 
    customerID INT UNSIGNED,
    offerCode VARCHAR(15),
    CONSTRAINT ordered_pk PRIMARY KEY(orderID),
    CONSTRAINT CustomerOrdered_fk FOREIGN KEY(customerID) REFERENCES Customer(customerID) ON UPDATE CASCADE,
    CONSTRAINT OfferOrdered_fk FOREIGN KEY(offerCode) REFERENCES Offer(offerCode) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Line_Item (
    itemNumber INT UNSIGNED,
    orderID INT UNSIGNED,
    Quantity TINYINT UNSIGNED,
    shippingAmount FLOAT(4,2),
    CONSTRAINT Line_Item_pk PRIMARY KEY(itemNumber, orderID),
    CONSTRAINT ItemLIneItem_fk FOREIGN KEY(itemNumber) REFERENCES Item(itemNumber) ON UPDATE CASCADE,
    CONSTRAINT OrderedLIneItem_fk FOREIGN KEY(orderID) REFERENCES Ordered(orderID) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Guarantee(
    orderID INT UNSIGNED,
    customerID INT UNSIGNED,
    url VARCHAR(50),
    refundAmount FLOAT(10, 2),
    CONSTRAINT PRIMARY KEY(orderID, customerID),
    CONSTRAINT OrderedGuarantee_fk FOREIGN KEY(orderID) REFERENCES Ordered(orderID) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT HomeGurantee_fk FOREIGN KEY(customerID) REFERENCES Home(customerID) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Purchase_Contact(
    contactName VARCHAR(50),
    customerID INT UNSIGNED,
    contactPhone CHAR(12) NOT NULL,
    CONSTRAINT PRIMARY KEY(contactName, customerID),
    CONSTRAINT BusinessPurchaseContact_fk FOREIGN KEY(customerID) REFERENCES Business(customerID) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- POPULATING THE TABLES: ACMEOnline Data

INSERT INTO Category
(categoryName, shippingPerPound, offersAllowed)
VALUES ('Books', 0.99, 'y'),
       ('Home', 1.99, 'y'),
	   ('Jewelry', 0.99, 'n'),
	   ('Toys', 0.99, 'y');
	   
INSERT INTO Item
(itemName, description, model, price, categoryName)
VALUES ('Cabbage Patch Doll', 'Baby boy doll', 'Boy', 39.95, 'Toys'),
       ('The Last Lecture', 'Written by Randy Pausch', 'Hardcover', 9.95, 'Books'),
	   ('Keuring Beverage Maker', 'Keurig Platnium Edition Beverage Maker in Red', 'Platinum Edition', 299.95, 'Home'),
	   ('1ct diamond ring in white gold', 'diamond is certified vvs, D, round', '64gt32', 4000.00, 'Jewelry');

INSERT INTO Offer
(offerCode, discountAmt, minAmount, expirationDate)
VALUES (345743213, '20% off', 20.00, '2013-12-31'),
       (4567890123, '30% off', 30.00, '2013-12-31');
	   
-- SINGLE TRANSACTIONS: Customer 1

START TRANSACTION;
	INSERT INTO Customer
	(customerName, address, email)
	VALUES ('Janine Jeffers','152 Lomb Memorial Dr., Rochester, NY 14623','jxj1234@rit.edu');
	INSERT INTO Home
	(customerID, creditCardNum, cardExpirationDate)
	VALUES (1, 1234567890123456, 012014);
	UPDATE Customer 
	SET customerType = 'Home' 
	WHERE customerName = 'Janine Jeffers';
	INSERT INTO Ordered
	(totalCost, offerCode)
	VALUES (4919.75, 4567890123);
	INSERT INTO Line_Item
	(orderID, itemNumber, quantity, shippingAmount)
	VALUES (1, 4, 1, .99),
		   (1, 2, 2, 3.99),
		   (1, 3, 3, 0.00);
COMMIT;

-- SINGLE TRANSACTIONS: Customer 2

START TRANSACTION;
	INSERT INTO Customer
	(customerName, address, email)
	VALUES ('Joey John Barber Shop','15 John St., Rochester, NY 14623', 'jj1978@hotmail.com');
	INSERT INTO Business
	(customerID, paymentTerms)
	VALUES (2, '30/90 days');
	UPDATE Customer
	SET customerType = 'Business'
	WHERE customerName = 'Joey John Barber Shop';
	INSERT INTO Ordered
	(totalCost, offerCode)
	VALUES (299.95, 345743213);
	INSERT INTO Line_Item
	(orderID, itemNumber, quantity, shippingAmount)
	VALUES (2, 3, 1, 0.00);
	INSERT INTO Purchase_Contact
	(customerID, contactName, contactPhone)
	VALUES (2, 'Joey James', '585-475-1234');
COMMIT;	











