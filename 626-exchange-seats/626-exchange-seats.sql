# Write your MySQL query statement below
SELECT CASE
           WHEN MOD(ID, 2) = 0 THEN ID - 1 
           WHEN MOD(ID, 2) != 0 AND ID != COUNTS THEN ID + 1
           ELSE ID END AS ID,
       STUDENT
FROM SEAT, 
(SELECT COUNT(*) AS COUNTS
FROM SEAT) AS SEAT_COUNTS
ORDER BY ID ASC