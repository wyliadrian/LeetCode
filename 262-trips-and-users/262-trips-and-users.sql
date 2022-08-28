# Write your MySQL query statement below
SELECT T.REQUEST_AT Day, ROUND(SUM(CASE T.STATUS WHEN "completed" THEN 0 ELSE 1 END)/COUNT(T.ID), 2) AS 'Cancellation Rate'
FROM TRIPS T
LEFT JOIN USERS U1
ON T.CLIENT_ID = U1.USERS_ID
LEFT JOIN USERS U2
ON T.DRIVER_ID = U2.USERS_ID
WHERE U1.BANNED = "No" AND U2.BANNED = "No" 
AND T.REQUEST_AT BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY T.REQUEST_AT