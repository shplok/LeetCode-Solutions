# Write your MySQL query statement below
SELECT distinct
    p.email
FROM
    Person as p
GROUP BY
    p.email 
    HAVING COUNT(*) > 1
