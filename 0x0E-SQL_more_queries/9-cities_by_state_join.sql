-- Lists all cities contained in the database hbtn_0d_usa.
-- sorted by cities.id
SELECT cities.id, cities.name, states.name
FROM cities
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
