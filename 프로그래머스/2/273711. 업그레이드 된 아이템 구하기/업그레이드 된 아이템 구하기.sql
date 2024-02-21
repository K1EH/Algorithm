-- 코드를 작성해주세요
SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
FROM ITEM_INFO AS A, ITEM_TREE AS B
WHERE A.ITEM_ID = B.ITEM_ID AND PARENT_ITEM_ID IN (SELECT ITEM_ID
                                             FROM ITEM_INFO
                                             WHERE RARITY = "RARE")
ORDER BY A.ITEM_ID DESC