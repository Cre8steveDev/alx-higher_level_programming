-- Using Inner Join to connect two tables that match on certain
-- Values, in this case join parts of the tables where the current
-- cities's value state_id is equal to the states table value.id

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
