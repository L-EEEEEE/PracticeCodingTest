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