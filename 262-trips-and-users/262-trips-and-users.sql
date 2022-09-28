# Write your MySQL query statement below
SELECT T.REQUEST_AT DAY,
       ROUND(SUM(IF(T.STATUS = "completed", 0, 1))/COUNT(T.ID), 2) 'Cancellation Rate'
FROM TRIPS T
LEFT JOIN USERS U1
ON T.CLIENT_ID = U1.USERS_ID
LEFT JOIN USERS U2
ON T.DRIVER_ID = U2.USERS_ID
WHERE U1.BANNED = "No"
AND U2.BANNED = "No"
AND T.REQUEST_AT BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY DAY