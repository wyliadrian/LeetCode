# Write your MySQL query statement below
SELECT Department, Employee, Salary FROM
(SELECT D.NAME Department, E.NAME Employee, E.SALARY Salary, RANK() OVER (PARTITION BY E.DEPARTMENTID ORDER BY E.SALARY DESC) RANKNUM
FROM EMPLOYEE E
LEFT JOIN DEPARTMENT D
ON E.DEPARTMENTID = D.ID) T
WHERE RANKNUM = 1