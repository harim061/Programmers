SELECT 
    SUM(SCORE) AS SCORE,
    G.EMP_NO,
    E.EMP_NAME,
    E.POSITION,
    E.EMAIL
    
    
FROM HR_GRADE G

JOIN HR_EMPLOYEES E ON E.EMP_NO = G.EMP_NO

WHERE YEAR = 2022

GROUP BY G.EMP_NO

ORDER BY SUM(SCORE) DESC
LIMIT 1;