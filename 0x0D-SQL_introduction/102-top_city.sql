-- Lists the top 3 cities with the highest average temperatures
-- during the months of July and August.
SELECT city, AVG(value) AS average_temperature
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
