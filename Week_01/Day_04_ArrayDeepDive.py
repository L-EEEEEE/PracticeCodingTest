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

# 연습 문제
# 문제 1. n개 간격의 원소들
# 정수 리스트 num_list와 정수 n이 주어집니다. num_list의 첫 번째 원소부터 시작하여 n개 간격으로 저장된 원소들을 차례로 담은 리스트를 return 하세요.
def solution(num_list, n):
    return num_list[::n]

# 테스트: [4, 2, 6, 1, 7, 6], 2 -> [4, 6, 7] 나와야 함
print(solution([4, 2, 6, 1, 7, 6], 2))


# 문제 2. 2차원으로 만들기 (★중요)
# 정수 배열 num_list와 정수 n이 주어집니다. num_list를 다음 설명과 같이 2차원 배열로 바꿔 return 하세요.
# num_list가 [1, 2, 3, 4, 5, 6, 7, 8]이고 n이 2라면, 2개씩 쪼개서 [[1, 2], [3, 4], [5, 6], [7, 8]]을 만듭니다.
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

# 테스트: [1, 2, 3, 4, 5, 6, 7, 8], 2 -> [[1, 2], [3, 4], [5, 6], [7, 8]]
print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))


# 문제 3. n 번째 원소부터
# 정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return 하세요.
# (주의: 인덱스 n이 아니라 'n번째'입니다. 인덱스로는 n-1 입니다.)
def solution(num_list, n):
    return num_list[n-1:]

# 테스트: [2, 1, 6], 3 -> [6] (3번째 원소인 6부터 끝까지)
print(solution([2, 1, 6], 3))