SELECT Department,Employee,Salary FROM
(
SELECT d.name as Department,e.name as Employee,e.salary AS Salary,
DENSE_RANK() OVER(Partition by d.name ORDER BY Salary DESC) ranks
FROM Employee e
LEFT JOIN Department d
ON e.departmentId=d.id
)t
WHERE ranks<4
ORDER BY Salary DESC;