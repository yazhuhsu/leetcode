-- PostgreSQL
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    WITH c AS (
        SELECT COUNT(DISTINCT(Employee.salary))
        FROM Employee
    )

    SELECT DISTINCT(Employee.salary)
    FROM Employee
    ORDER BY Employee.salary DESC
    LIMIT 1 OFFSET CASE WHEN N > 0 THEN N-1 ELSE (SELECT count FROM c) END
  );
END;
$$ LANGUAGE plpgsql;