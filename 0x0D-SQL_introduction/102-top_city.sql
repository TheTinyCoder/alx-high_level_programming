-- select a certain number of rows from records
-- SOURCE temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
