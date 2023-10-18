-- Import in hbtn_0c_0 database this table dump
-- Display the average temperature of the cities
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
