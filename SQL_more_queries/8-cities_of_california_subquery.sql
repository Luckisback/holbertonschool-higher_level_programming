-- A script that lists all the cities coming from an other table

SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC; 
