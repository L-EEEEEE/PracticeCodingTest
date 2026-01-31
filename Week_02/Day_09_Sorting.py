arr = [3, 1, 5, 2]

# 1. sort(): 원본을 바꿈 (반환값 없음)
arr.sort()
print(arr) # [1, 2, 3, 5]

# 2. sorted(): 원본은 그대로 두고, 정렬된 새 리스트를 반환
arr = [3, 1, 5, 2]
new_arr = sorted(arr)
print(arr)     # [3, 1, 5, 2] (그대로)
print(new_arr) # [1, 2, 3, 5] (정렬됨)




words = ["apple", "b", "cat", "drone"]

# 1. 길이(len) 순으로 정렬
# 해석: 각 원소(x)의 길이(len(x))를 기준으로 줄을 세워라
words.sort(key=lambda x: len(x))
print(words) # ['b', 'cat', 'apple', 'drone']

# 2. 다중 조건 정렬 (튜플 사용)
# 조건: "길이 순으로 먼저 하고, 길이가 같으면 사전 순으로 해라"
words = ["apple", "b", "cat", "car"]
words.sort(key=lambda x: (len(x), x))
print(words) # ['b', 'car', 'cat', 'apple'] ('car'가 'cat'보다 앞)