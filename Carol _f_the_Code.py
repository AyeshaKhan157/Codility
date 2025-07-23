def solution(A):
    N = len(A)
    rot = [[(tile[-r:] + tile[:-r], min(r, 4 - r)) for r in range(4)] for tile in A]
    
    dp = [[float('inf')] * 4 for _ in range(N)]
    for r in range(4):
        dp[0][r] = rot[0][r][1]  

    for i in range(1, N):
        for r in range(4):
            curr, cost = rot[i][r]
            for k in range(4):
                prev, _ = rot[i-1][k]
                if prev[1] == curr[3]: 
                    dp[i][r] = min(dp[i][r], dp[i-1][k] + cost)

    return min(dp[-1])
