-- list number of records with same score value
SELECT score, COUNT(score) AS number FROM second_table ORDER BY number DESC;
