-- list number of records with same score value
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
