--a script that lists all the cities coming from an other table

--SELECT id, name FROM cities
--WHERE state_id = (SELECT id FROM states WHERE name = "California"),
--ORDER BY id ASC; 

SELECT id, name FROM cities WHERE state_id = 1 ORDER BY cities.id ASC;
