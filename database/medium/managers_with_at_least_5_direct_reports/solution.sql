SELECT managers.name
FROM (
    SELECT E.managerId, COUNT(E.managerId) AS count
    FROM (
        SELECT 
            Employee.id, 
            Employee.name, 
            Employee.department, 
            CASE WHEN managerId IS NULL THEN Employee.id ELSE Employee.managerId END
        FROM Employee
    ) AS E
    GROUP BY E.managerId
) AS ems
INNER JOIN (
    SELECT id, name
    FROM Employee
) managers ON managers.id = ems.managerId
WHERE count >= 5