-- select e.name as Employee
-- from Employee as e
-- where (e.managerid is not NULL) and 
--         (e.salary > (select e2.salary from Employee as e2 where e2.managerid is NULL and e2.id = e.managerid));

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
