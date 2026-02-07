# SELECT ANIMAL_TYPE, COUNT(*)
# FROM ANIMAL_INS
# GROUP BY ANIMAL_TYPE;
# -- 결과: Cat | 3, Dog | 2
#
#
# SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
# FROM ANIMAL_INS
# GROUP BY ANIMAL_TYPE -- 종류별로 묶어라
# ORDER BY ANIMAL_TYPE; -- Cat이 C니까 먼저 나옴 (오름차순)

# WHERE: 그룹으로 묶기 전에, 각 행(Row)을 필터링 (예: 아픈 동물 제외)
# HAVING: 그룹으로 묶은 후에, 그룹 자체를 필터링 (예: 2마리 이상인 그룹만 조회)