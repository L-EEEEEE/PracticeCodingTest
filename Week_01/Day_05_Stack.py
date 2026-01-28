stack = []

# 1. 넣기 (Push)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack) # [1, 2, 3]

# 2. 맨 위 확인 (Peek)
print(stack[-1]) # 3 (꺼내진 않음)

# 3. 빼기 (Pop)
top = stack.pop()
print(top)   # 3 (꺼내짐)
print(stack) # [1, 2] (3이 사라짐)


# 연습문제
# 문제 1. 컨트롤 제트 (Programmers Lv.0 기출)
# 숫자와 문자 "Z"가 공백으로 구분되어 담긴 문자열 s가 주어집니다.
# 문자열에 있는 숫자를 차례대로 더하되, "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 최종 합계를 return 하세요.
def solution(s):
    stack = []
    for i in s.split():
        if i == "Z":
            stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)

# 테스트
print(solution("1 2 Z 3"))      # 4 (1 + 2 - 2 + 3)
print(solution("10 20 30 40"))  # 100
print(solution("10 Z 20 Z 1"))  # 1

# 문제 2. 올바른 괄호
# 괄호가 바르게 짝지어졌는지 확인하는 문제입니다. "(()"는 짝이 안 맞고, "()()"는 맞습니다.
# 여는 괄호 (는 스택에 넣고, 닫는 괄호 )를 만나면 스택에서 뺍니다.
def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else: # ')' 인 경우
            if not stack: # 스택이 비어있는데 닫는 괄호가 나오면 에러
                return False
            stack.pop() # 짝이 맞으니 스택에서 뺀다

    # 반복문이 끝났는데 스택에 괄호가 남아있으면 짝이 안 맞음
    return len(stack) == 0

# 테스트
print(solution("()()"))  # True
print(solution("(())()")) # True
print(solution(")()("))  # False (닫는 괄호가 먼저 옴)
print(solution("(()("))  # False (여는 괄호가 남음)