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

# 연습문제
# 문제 1. 배열 회전시키기 (Programmers Lv.0)
# 정수가 담긴 배열 numbers와 문자열 direction("left" 또는 "right")이 주어집니다. 배열을 해당 방향으로 한 칸씩 회전시킨 배열을 return 하세요.
# 예: [1, 2, 3], "right" -> [3, 1, 2] (맨 뒤 숫자가 앞으로)
# 예: [4, 5, 6], "left" -> [5, 6, 4] (맨 앞 숫자가 뒤로)
from collections import deque

def solution(numbers, direction):
    # 1. numbers를 deque로 변환
    queue = deque(numbers)

    # 2. direction에 따라 회전 (rotate 활용 추천)
    if direction == "right":
        # 오른쪽으로 회전
        queue.rotate(1)
        pass
    else:
        # 왼쪽으로 회전
        queue.rotate(-1)
        pass

    # 3. 다시 리스트로 바꿔서 반환
    return list(queue)

# 테스트
print(solution([1, 2, 3], "right")) # [3, 1, 2]
print(solution([4, 5, 6], "left"))  # [5, 6, 4]


# 문제 2. N번째 원소 삭제 (큐의 순환)
# 1번부터 N번까지의 숫자가 원 모양으로 앉아있습니다. K번째 사람을 한 명씩 제거할 때, 마지막에 남는 숫자를 구하는 문제입니다.
# (요세푸스 문제의 간소화 버전)
# 입력: N=5, K=2 (1~5번 사람, 2번째 사람마다 제거)
# 과정:
# [1, 2, 3, 4, 5] -> 1번 패스(뒤로 보냄), 2번 제거 -> [3, 4, 5, 1]
# [3, 4, 5, 1] -> 3번 패스, 4번 제거 -> [5, 1, 3]
# 반복...
from collections import deque

def solution(N, K):
    queue = deque(range(1, N + 1)) # [1, 2, ..., N]

    while len(queue) > 1: # 한 명이 남을 때까지 반복
        # K-1번 만큼 앞에서 빼서 뒤로 보냄 (rotate 써도 됨)
        for _ in range(K - 1):
            val = queue.popleft()
            queue.append(val)

        # K번째 사람 제거 (영구 삭제)
        queue.popleft()

    return queue[0] # 마지막 남은 사람

# 테스트: 5명 중 2번째마다 제거 -> 3이 남아야 함
print(solution(5, 2))