-- Write a script that lists the number of records with the same score in the table second_table of the database 

SELECT score, COUNT(*) AS number
GROUP BY score ORDER BY number DESC;