-- import table dump from sql and display max temp by state
-- SOURCE temperatures.sql
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
