# 문제 1. 같은 숫자는 싫어 (스택 활용)
# 배열 arr가 주어집니다. 배열에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
# 단, 제거된 후 남은 수들을 반환할 때는 원래 배열의 순서를 유지해야 합니다.
# 입력: [1, 1, 3, 3, 0, 1, 1]
# 출력: [1, 3, 0, 1] (연속된 것만 삭제, 뒤에 나온 1은 연속되지 않으므로 유지)
def solution(arr):
    stack = []
    for num in arr:
        # 스택이 비어있지 않고, 마지막 넣은 값이 현재 값과 같으면 -> 패스
        if len(stack) > 0 and stack[-1] == num:
            continue
        stack.append(num)
    return stack

# 테스트
print(solution([1, 1, 3, 3, 0, 1, 1])) # [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3]))       # [4, 3]


# 문제 2. 카드 뭉치 (큐 활용)
# 코니는 영어 단어가 적힌 카드 뭉치 두 개(cards1, cards2)를 가지고 있습니다. 이 카드를 순서대로 한 장씩 사용하여 원하는 문장(goal)을 만들 수 있는지 확인하세요.
# 규칙: 카드는 한 번에 한 장씩만 쓸 수 있고, 뭉치에서 꺼낸 카드는 다시 넣을 수 없습니다. (즉, Queue의 popleft와 같습니다)
# 예시:
# cards1: ["i", "drink", "water"]
# cards2: ["want", "to"]
# goal: ["i", "want", "to", "drink", "water"]
# 결과: "Yes" (가능함)
from collections import deque

def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)

    for word in goal:
        if q1 and q1[0] == word: # q1 확인
            q1.popleft()
        elif q2 and q2[0] == word: # q2 확인
            q2.popleft()
        else: # 둘 다 없으면 실패
            return "No"

    return "Yes"

# 테스트
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # Yes
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])) # No


# [도전] 문제 3. 크레인 인형 뽑기 (통합형)
# board: N * N 크기의 격자에 인형이 들어있습니다. (0은 빈칸, 숫자는 인형 종류)
# moves: 크레인을 작동시킬 위치(열 번호)가 담긴 배열입니다.
# 크레인은 해당 열의 가장 위에 있는 인형을 집어서 바구니(stack)에 넣습니다.
# 바구니에 같은 모양 인형 2개가 연속으로 쌓이면 둘 다 터집니다.
# 터진 인형의 총 개수를 구하세요.
def solution(board, moves):
    stack = [] # 바구니
    answer = 0 # 터진 인형 개수

    # moves에 있는 번호(열)를 하나씩 가져옴
    for move in moves:
        col = move - 1 # 인덱스는 0부터 시작하므로 -1

        # 해당 열(col)에서 위에서부터(row 0 -> N) 내려가며 인형 찾기
        for row in range(len(board)):
            if board[row][col] != 0: # 인형이 있으면(0이 아니면)
                doll = board[row][col] # 인형 집기
                board[row][col] = 0    # 집었으니 빈칸(0)으로 만듦

                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)

                break # 인형 하나 집었으면 다음 move로 넘어가야 함 (안쪽 for문 종료)

    return answer