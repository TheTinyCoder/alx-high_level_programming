-- list number of records with same score value
SELECT score, COUNT(*) AS number FROM second_table ORDER BY number DESC;
