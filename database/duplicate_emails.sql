SELECT DISTINCT p1.`Email`
FROM `Person` p1
INNER JOIN (
    SELECT `Email`, COUNT(*)
    FROM `Person`
    GROUP BY `Email`
    HAVING COUNT(*) > 1
) p2 ON p1.`Email` = p2.`Email`