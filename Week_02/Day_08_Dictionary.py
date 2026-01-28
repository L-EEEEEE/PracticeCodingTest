# 빈 딕셔너리 생성 (Key: Value 구조)
menu = {}

# 1. 데이터 넣기 & 수정
menu["Burger"] = 5000
menu["Coke"] = 2000
print(menu) # {'Burger': 5000, 'Coke': 2000}

# 2. 값 확인하기 (in 연산자) ★ 중요
if "Burger" in menu:
    print("버거 있어요!")

# 3. 개수 세기 패턴 (get 함수) ★★★ 무조건 암기!
# menu.get(키, 기본값): 키가 있으면 해당 값을, 없으면 기본값(0)을 가져옴
# 해석: "Coke의 원래 개수 가져와서 1 더해줘. 없으면 0개부터 시작해."
menu["Coke"] = menu.get("Coke", 0) + 1
print(menu["Coke"]) # 2001 (기존 값 + 1)

# 연습문제
# 문제 1. 완주하지 못한 선수 (Lv.1 필수)
# 마라톤 참여자 명단 participant와 완주자 명단 completion이 주어집니다. 완주하지 못한 단 한 명의 선수 이름을 return 하세요. (동명이인이 있을 수 있습니다.)
# 입력: ["leo", "kiki", "eden"], ["eden", "kiki"]
# 출력: "leo"
def solution(participant, completion):
    hash_map = {}

    # 1. 참가자 이름 세기 (Hash 만들기)
    for p in participant:
        hash_map[p] = hash_map.get(p, 0) + 1

    # 2. 완주자 이름 빼기
    for c in completion:
        hash_map[c] -= 1

    # 3. 개수가 0이 아닌(남아있는) 사람 찾기
    for key, val in hash_map.items():
        if val > 0:
            return key

# 테스트
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # "mislav"


# 문제 2. 폰켓몬 (Set 활용)
# 당신은 N마리의 폰켓몬 중 N/2마리를 가져갈 수 있습니다. 최대한 다양한 종류의 폰켓몬을 가져가려 합니다. 가져갈 수 있는 폰켓몬 종류 수의 최댓값을 구하세요.
# 입력: [3, 1, 2, 3] (총 4마리 -> 2마리 선택 가능)
# 종류: 1번, 2번, 3번 (총 3종류)전략: 3종류가 있지만, 나는 2마리밖에 못 가져가므로 최대 종류 수는 2입니다.
def solution(nums):
    # 1. 가져갈 수 있는 마릿수 (N / 2)
    pick_num = len(nums) // 2

    # 2. 폰켓몬의 종류 개수 (중복 제거)
    unique_types = len(set(nums))

    # 3. 둘 중 더 작은 값이 정답!
    # (종류가 아무리 많아도 pick_num만큼만 가져갈 수 있고,
    #  가져갈 자리가 많아도 종류가 적으면 그게 최대니까요.)
    return min(pick_num, unique_types)

# 테스트
print(solution([3, 1, 2, 3])) # 2
print(solution([3, 3, 3, 2, 2, 4])) # 3


# 문제 3. 가장 가까운 같은 글자 (문자열+해시)
# 문자열 s가 주어질 때, 각 문자가 자신보다 앞에 나왔던 같은 글자와 얼마나 떨어져 있는지 구하세요. (처음 나왔으면 -1)
# 입력: "banana"
# 과정:
#   b: 처음 나옴 -> -1
#   a: 처음 나옴 -> -1
#   n: 처음 나옴 $\rightarrow$ -1
#   a: 앞에 a가 있었음(인덱스 1). 현재(3) - 과거(1) = 2
#   n: 앞에 n이 있었음(인덱스 2). 현재(4) - 과거(2) = 2
#   a: 앞에 a가 있었음(인덱스 3). 현재(5) - 과거(3) = 2
# 출력: [-1, -1, -1, 2, 2, 2]
def solution(s):
    answer = []
    # 키: 글자, 값: 마지막으로 등장한 인덱스 위치
    last_pos = {}

    for i, char in enumerate(s): # i는 인덱스, char는 글자
        if char not in last_pos:
            answer.append(-1)
        else:
            # 현재 위치(i) - 마지막 위치(last_pos[char])
            answer.append(i - last_pos[char])

        # 현재 위치를 최신으로 업데이트 ★ 중요
        last_pos[char] = i
    return answer

# 테스트
print(solution("banana"))
print(solution("foobar"))