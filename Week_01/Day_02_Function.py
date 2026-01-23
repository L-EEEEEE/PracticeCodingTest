# 기본 구조
def solution(num1, num2):
    # 여기에 로직 작성
    answer = num1 + num2
    return answer  # 결과값을 반드시 return 해야 함 (print 아님!)

# 문자열 (String) 관련
text = "Hello Python"
# 1. 특정 문자 바꾸기 / 제거하기 (replace) ★★★
# 사용법: 문자열.replace("찾을문자", "바꿀문자")
print(text.replace("Python", "World"))  # "Hello World"
print(text.replace(" ", ""))            # "HelloPython" (공백 제거할 때 많이 씀)

# 2. 대소문자 변환 (upper, lower)
print(text.upper())  # "HELLO PYTHON" (대소문자 무시하고 비교할 때 필수)
print(text.lower())  # "hello python"

# 3. 개수 세기 (count)
print(text.count("o"))  # 2 (o가 2개 있음)



# 리스트 (List) 관련
arr = [3, 1, 5, 2]

# 1. 데이터 추가 (append) ★★★
arr.append(10)
print(arr)  # [3, 1, 5, 2, 10]

# 2. 정렬하기 (sort) ★★★
arr.sort()             # 오름차순 정렬 (원본이 바뀜)
print(arr)             # [1, 2, 3, 5, 10]

arr.sort(reverse=True) # 내림차순 정렬
print(arr)             # [10, 5, 3, 2, 1]

# 3. 길이 재기 (len) - 문자열도 가능
print(len(arr))        # 5