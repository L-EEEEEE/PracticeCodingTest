def solution(n, lost, reserve):
    # 1. 중복 제거 (여벌 있는데 도난당한 애들은 제외)
    # set을 쓰면 차집합 연산(-)이 가능해 매우 편리
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)

    # 2. 빌려주기 (앞 번호부터 차례대로 빌려줘야 최대로 빌릴 수 있음 -> 정렬 필요?)
    # set은 순서가 없으므로 for문 돌릴 때 정렬해서 처리하는 게 안전
    for r in sorted(real_reserve):
        # 앞 번호 학생이 잃어버렸으면 빌려줌
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        # 뒷 번호 학생이 잃어버렸으면 빌려줌
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)

    # 전체 학생 수 - 끝까지 못 빌린 학생 수
    return n - len(real_lost)

# 테스트
print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3]))       # 4



