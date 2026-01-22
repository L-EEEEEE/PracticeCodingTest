# 1. 정수 1개 받기 (예: 5)
N = int(input())


# 2. 문자열 1개 받기 (예: hello)
S = input()

# 3. 공백으로 구분된 숫자 여러 개 받기 (예: 10 20 30) ★ 가장 많이 쓰임
# map(int, ...)는 입력받은 문자를 모두 숫자로 바꿈
a, b, c = map(int, input().split())

# 4. 숫자 리스트로 한 번에 받기 (예: 1 2 3 4 5) ★ 필수 암기
nums = list(map(int, input().split()))

print(N)
print(nums) # 결과: [1, 2, 3, 4, 5]


# 조건문
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B") # 실행됨
else:
    print("C")

# Tip: 조건문 안에는 '논리 연산자'가 자주 쓰입니다.
# and (둘 다 참), or (하나라도 참), not (반대)
if score >= 80 and score < 90:
    print("B학점 입니다.")

# 반복문
# 1. 횟수 반복 (0부터 4까지, 총 5번)
# range(5) -> 0, 1, 2, 3, 4
for i in range(5):
    print(i, end=" ") # 출력: 0 1 2 3 4
print()

# 2. 범위 반복 (1부터 10까지)
# range(시작, 끝+1) -> 끝 숫자는 포함되지 않음 주의!
for i in range(1, 6):
    print(i, end=" ") # 출력: 1 2 3 4 5
print()

# 3. 리스트 순회 (가장 많이 씀)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # 리스트 안의 요소를 하나씩 꺼냄


#문자열 조작
text = "Coding Test"

# 1. 슬라이싱 (Slicing) - 문자열 자르기
print(text[0:6])   # "Coding" (0번부터 5번 인덱스까지)
print(text[::-1])  # "tseT gnidoC" (문자열 뒤집기 - 자주 나옴!)

# 2. 쪼개기 (Split) - 문자열을 리스트로 변환
data = "10:20:30"
time_list = data.split(":")
print(time_list) # ['10', '20', '30']

# 3. 합치기 (Join) - 리스트를 문자열로 변환
result = "-".join(time_list)
print(result) # "10-20-30"