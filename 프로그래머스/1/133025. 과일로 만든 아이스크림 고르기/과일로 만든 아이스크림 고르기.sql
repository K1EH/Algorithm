-- 코드를 입력하세요
SELECT A.FLAVOR
FROM FIRST_HALF AS A, ICECREAM_INFO AS B
WHERE A.FLAVOR = B.FLAVOR AND B.INGREDIENT_TYPE LIKE "FRUIT%" AND A.TOTAL_ORDER >= 3000
ORDER BY TOTAL_ORDER DESC