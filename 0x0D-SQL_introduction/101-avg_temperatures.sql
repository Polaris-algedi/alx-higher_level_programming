-- Retrieves the average temperature (in Fahrenheit)
-- for each city, sorted in descending order of temperature.
SELECT city, AVG(value) AS average_temperature
FROM temperatures GROUP BY city
ORDER BY average_temperature DESC;
