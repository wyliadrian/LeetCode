# Write your MySQL query statement below
SELECT A1.PLAYER_ID, A1.EVENT_DATE, SUM(A2.GAMES_PLAYED) GAMES_PLAYED_SO_FAR
FROM ACTIVITY A1, ACTIVITY A2
WHERE A1.PLAYER_ID = A2.PLAYER_ID
AND A1.EVENT_DATE >= A2.EVENT_DATE
GROUP BY A1.PLAYER_ID, A1.EVENT_DATE