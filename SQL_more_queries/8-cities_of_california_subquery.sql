--a script that lists all the cities coming from an other table

SELECT state_id, name FROM cities
WHERE state_id = (
		SELECT id FROM states
		WHERE name = 'California');
