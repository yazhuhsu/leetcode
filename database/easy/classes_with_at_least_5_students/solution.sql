SELECT class FROM (
    SELECT class, count(student) 
    FROM Courses
    GROUP BY class
) AS summary WHERE summary.count >= 5