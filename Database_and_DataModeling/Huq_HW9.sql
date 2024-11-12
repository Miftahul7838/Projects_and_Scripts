-- Name: Miftahul Huq
-- Date: 04/18/2022
-- Course: ISTS-230

-- Use Book database 
USE book;

-- Question 1
SELECT CONCAT(city, ',', stateCode) AS "Location", COUNT(publisherID)
FROM publisher
GROUP BY city, stateCode
ORDER BY COUNT(publisherID) ASC, CONCAT(city, ',', statecode) DESC;

-- Question 2

SELECT title, COUNT(rating) AS "Total Rating", MIN(rating) AS "Low", MAX(rating) AS "Max", ROUND(AVG(rating),2) AS "Average"
FROM book LEFT JOIN bookReview
ON book.isbn = bookReview.isbn
GROUP BY title
ORDER BY COUNT(rating) DESC, AVG(rating) DESC; 

-- Question 3
SELECT publisher.name AS "Publisher Name", COUNT(book.isbn) AS "Book Count"
FROM publisher JOIN book
ON publisher.publisherID = book.publisherID
GROUP BY publisher.name
HAVING COUNT(book.isbn) > 2
ORDER BY COUNT(book.isbn) DESC, publisher.name ASC;

-- Question 4

SELECT title, LENGTH(title) AS "Length", SUBSTR(title, INSTR(title, 'bill') + 4) AS "After Bill"
FROM book 
WHERE title LIKE '%bill%'
ORDER BY title DESC;

-- Question 5

SELECT DISTINCT book.title
FROM ownersBook INNER JOIN book
ON ownersBook.isbn = book.isbn
GROUP BY book.title
ORDER BY title DESC;





