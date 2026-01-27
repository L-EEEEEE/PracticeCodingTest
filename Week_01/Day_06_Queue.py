# 필수 라이브러리 불러오기
from collections import deque

# 1. 큐 생성
queue = deque([1, 2, 3])

# 2. 데이터 넣기 (뒤로 줄 서기)
queue.append(4)
print(queue) # deque([1, 2, 3, 4])

# 3. 데이터 빼기 (맨 앞사람 나가기) ★ 핵심
front = queue.popleft() # pop(0) 대신 이걸 씁니다!
print(front) # 1
print(queue) # deque([2, 3, 4])

# 4. 회전하기 (보너스 꿀팁)
# 양수로 넣으면 오른쪽(시계방향) 회전, 음수는 왼쪽 회전
queue.rotate(1)
print(queue) # deque([4, 2, 3]) -> 맨 뒤의 4가 앞으로 옴