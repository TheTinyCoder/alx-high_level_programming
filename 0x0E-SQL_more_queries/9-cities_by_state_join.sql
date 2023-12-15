-- list all cities and their state by name
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON cities.state_id = states.id;
