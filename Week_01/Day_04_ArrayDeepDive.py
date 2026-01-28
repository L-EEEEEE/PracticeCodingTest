nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. 2칸씩 건너뛰며 가져오기 (짝수 인덱스)
print(nums[::2])  # [0, 2, 4, 6, 8]

# 2. 홀수 인덱스만 가져오기 (1번부터 시작해서 2칸씩)
print(nums[1::2]) # [1, 3, 5, 7, 9]

# 3. 거꾸로 출력하기 (간격이 -1이면 뒤집기)
print(nums[::-1]) # [9, 8, ... , 0]


# range(시작, 끝, 간격)
# 0부터 9까지, 3씩 증가 -> 0, 3, 6, 9
for i in range(0, 10, 3):
    print(i, end=" ")
    # 출력: 0 3 6 9


arr1 = [1, 2]
arr2 = [3, 4]

# Case 1: append (리스트 자체를 하나의 '요소'로 넣음)
arr1.append(arr2)
print(arr1) # [1, 2, [3, 4]] -> 2차원이 됨 (주의!)

# Case 2: extend 또는 + 연산자 (리스트를 풀어서 '연결'함)
arr1 = [1, 2]
arr1.extend(arr2) # 또는 arr1 += arr2
print(arr1) # [1, 2, 3, 4] -> 우리가 보통 원하는 것


# 연습문제
# 문제 1. 배열 자르기 (Slicing 활용)
def solution(numbers, num1, num2):
    return numbers[num1 : num2 + 1]

# 테스트: [1, 2, 3, 4, 5], 1, 3 입력 시 -> [2, 3, 4] 나와야 함
print(solution([1, 2, 3, 4, 5], 1, 3))


# 문제 2. 배열 원소의 길이 (List Comprehension 활용 추천)
def solution(strlist):
    answer = [len(i) for i in strlist]
    return answer

# 테스트: ["We", "are", "the", "world!"] -> [2, 3, 3, 6] 나와야 함
print(solution(["We", "are", "the", "world!"]))


# 문제 3. 가장 큰 수 찾기 (기초 내장함수)
def solution(array):
    max_val = max(array)       # 가장 큰 수 찾기
    idx = array.index(max_val) # 그 수가 몇 번째에 있는지 찾기
    return [max_val, idx]

# 테스트: [1, 8, 3] -> [8, 1] 나와야 함 (8이 가장 크고, 1번 인덱스에 있음)
print(solution([1, 8, 3]))
