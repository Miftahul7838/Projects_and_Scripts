-- Date updated: 02/07/2022
-- BY: Miftahul Huq
-- Course: ISTE 230

-- Question #1
SELECT headOfState
FROM country
WHERE name = 'United States';

-- Questions #2
Update country 
SET headOfState = 'Joseph R. Biden'
WHERE name = 'United States';

-- Rerun query from Question #1
SELECT headOfState
FROM country
WHERE name = 'United States';

-- Question #3 
SELECT name
FROM country
WHERE indepYear IS NULL;

-- Question #4
SELECT name, continent
FROM country
WHERE (population > 1000000000) AND (lifeExpectancy BETWEEN 70 AND 80);

-- Question #5
SELECT name
FROM country
WHERE continent = 'North America' OR continent = 'South America';

