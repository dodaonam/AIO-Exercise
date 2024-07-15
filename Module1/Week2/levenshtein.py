def levenshtein_distance(s, t):
    M = len(s)
    N = len(t)
    D = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(N + 1):
        D[0][i] = i
    for j in range(M + 1):
        D[j][0] = j
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if s[i - 1] == t[j - 1]:
                sub_cost = 0
            else:
                sub_cost = 1
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + sub_cost)
    return D[M][N]


print(levenshtein_distance('yu', 'you'))