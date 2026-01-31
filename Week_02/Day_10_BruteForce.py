from itertools import permutations, combinations

nums = [1, 2, 3]

# 1. 순열 (Permutations): 순서 중요! (1, 2) != (2, 1)
# 3개 중 2개를 뽑아 줄 세우기
perm = list(permutations(nums, 2))
print(perm) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 2. 조합 (Combinations): 순서 상관없음! (1, 2) == (2, 1)
# 3개 중 2개를 뽑기만 하기
comb = list(combinations(nums, 2))
print(comb) # [(1, 2), (1, 3), (2, 3)]

