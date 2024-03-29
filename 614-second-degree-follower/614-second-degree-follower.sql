# Write your MySQL query statement below
SELECT FOLLOWEE AS FOLLOWER, COUNT(FOLLOWEE) AS NUM
FROM FOLLOW 
WHERE FOLLOWEE IN
(SELECT DISTINCT A.FOLLOWER FROM FOLLOW A, FOLLOW B
WHERE A.FOLLOWER = B.FOLLOWEE)
GROUP BY FOLLOWEE
ORDER BY FOLLOWER