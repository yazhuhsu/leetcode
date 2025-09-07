SELECT Scores.score, s.rank 
FROM Scores
LEFT JOIN (
    SELECT score, row_number() over (ORDER BY score DESC) AS rank
    FROM Scores
    GROUP BY score
) s ON s.score = Scores.score
ORDER BY Scores.score DESC
