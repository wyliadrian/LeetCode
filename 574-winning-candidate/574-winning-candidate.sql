# Write your MySQL query statement below
SELECT NAME FROM CANDIDATE,
(SELECT CANDIDATEID, COUNT(ID) VOTES FROM VOTE GROUP BY CANDIDATEID ORDER BY VOTES DESC LIMIT 1) V
WHERE ID = V.CANDIDATEID