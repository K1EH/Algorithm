SET @HOUR_LIST = -1;
SELECT (@HOUR_LIST := @HOUR_LIST + 1) AS HOUR , 
        (SELECT COUNT(*)
         FROM ANIMAL_OUTS
         WHERE hour(DATETIME) = @HOUR_LIST) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR_LIST < 23;