# Date updated: 01/27/2022

-- Drops the HW2 databse if it exists

DROP DATABASE IF EXISTS HW2;
CREATE DATABASE HW2;
USE HW2;

-- Creates the item table

/* Since the database is dropped if it exists,
   there is no reason to drop the table */
   
CREATE TABLE item(

itemID VARCHAR(25)				COMMENT "This will be the Primary Key",
itemName VARCHAR(25),
name VARCHAR(25),
street VARCHAR(25),
city VARCHAR(25),
colors VARCHAR(25),
state CHAR(2),
zipcode VARCHAR(10),
cost VARCHAR(10),
retailPrice VARCHAR(10),
notes VARCHAR(255),
description VARCHAR(255),
returnable CHAR(1),
perishable CHAR(1),
shelfQty INT,

CONSTRAINT item_pk PRIMARY KEY(itemID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;