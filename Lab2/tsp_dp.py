n = 5

dist = [[0, 12, 10, 19, 8],
        [12, 0, 3, 7, 6],
        [10, 3, 0, 2, 20],
        [19, 7, 2, 0, 4],
        [8, 6, 20, 4, 0]]
        
complete = (1 << n) - 1

dp = [[-1 for _ in range(n)] for _ in range(2 ** n)]

def TSP(mark, position):
    if mark == complete:
        return dist[position][0]
    if dp[mark][position] != -1:
        return dp[mark][position]
    ans = float('inf')
    for city in range(n):
        if not (mark & (1 << city)):
            newAns = dist[position][city] + TSP(mark | (1 << city), city)
            ans = min(ans, newAns)
    dp[mark][position] = ans
    return ans

print("Minimum cost to travel all cities:", TSP(1, 0))