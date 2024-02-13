-- count and group the numbe rof a particular data

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
