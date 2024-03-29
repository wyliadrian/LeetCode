# Write your MySQL query statement below
SELECT PLAYER_ID, DEVICE_ID FROM
(SELECT PLAYER_ID, DEVICE_ID, ROW_NUMBER() OVER (PARTITION BY PLAYER_ID ORDER BY EVENT_DATE ASC) ROWNUM FROM ACTIVITY) T
WHERE ROWNUM = 1