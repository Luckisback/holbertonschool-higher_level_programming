--a script that lists all the cities coming from an other table

SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE id = 1 AND name = "California";),
ORDER BY id ASC; 
