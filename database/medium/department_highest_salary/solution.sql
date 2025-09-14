SELECT Department.name AS Department, Employee.name AS Employee, Employee.salary AS Salary
FROM Employee
INNER JOIN(
    SELECT Employee.departmentId AS id, MAX(Employee.salary) AS salary
    FROM Employee
    GROUP BY Employee.departmentId
) M ON M.id = Employee.departmentId AND M.salary = Employee.Salary
INNER JOIN Department ON Department.id = Employee.departmentId 