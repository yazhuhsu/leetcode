-- Write your PostgreSQL query statement below
SELECT id FROM (
    SELECT id, recordDate, temperature, 
        CEILING(EXTRACT(EPOCH FROM recordDate) - EXTRACT(EPOCH FROM LAG(recordDate) OVER (ORDER BY recordDate))) / (24 * 60 * 60) AS day_diff,
        temperature - LAG(temperature) OVER (ORDER BY recordDate) AS temperature_diff
    FROM Weather
) WHERE temperature_diff > 0 AND day_diff = 1 ORDER BY id ASC