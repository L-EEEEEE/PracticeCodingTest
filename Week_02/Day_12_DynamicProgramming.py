def solution(n):
    # 1. DP 테이블 생성 (0부터 n까지니까 n+1개)
    dp = [0] * (n + 1)

    # 2. 초기값 설정
    dp[0] = 0
    dp[1] = 1

    # 3. 점화식 적용 (2부터 n까지)
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n]

# 테스트
print(solution(3)) # 2 (0, 1, 1, 2)
print(solution(5)) # 5 (0, 1, 1, 2, 3, 5)