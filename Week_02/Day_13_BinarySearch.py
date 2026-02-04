from bisect import bisect_left, bisect_right

nums = [1, 2, 4, 4, 8]

# 1. bisect_left(배열, 찾을값): 찾을 값이 들어갈 '가장 왼쪽' 위치(인덱스) 반환
print(bisect_left(nums, 4))  # 2 (인덱스 2에 있는 4 앞)

# 2. bisect_right(배열, 찾을값): 찾을 값이 들어갈 '가장 오른쪽' 위치 반환
print(bisect_right(nums, 4)) # 4 (인덱스 3에 있는 4 뒤)

# 응용: 특정 범위(4)의 개수 구하기
# 4의 개수 = bisect_right(4) - bisect_left(4)
print(bisect_right(nums, 4) - bisect_left(nums, 4)) # 4 - 2 = 2개