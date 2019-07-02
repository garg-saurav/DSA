# pseudo code taken from CLRS book

def lcs(X, Y):
    c = {}  # c[(i,j)] represents length of lcs of [x0, x1, ... , xi] and [y0, y1, ... , yj]
    m = len(X)
    n = len(Y)
    for i in range(m):
        c[(i, -1)] = 0
    for j in range(n):
        c[(-1, j)] = 0
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                c[(i, j)] = 1 + c[(i-1, j-1)]
            elif c[(i-1, j)] >= c[(i, j-1)]:
                c[(i, j)] = c[(i-1, j)]
            else:
                c[(i, j)] = c[(i, j-1)]
    lcs = []
    i = m-1
    j = n-1
    while (i != -1 and j != -1):
        if X[i] == Y[j]:
            lcs = [X[i]] + lcs
            i -= 1
            j -= 1
        elif c[(i, j)] == c[(i-1, j)]:
            i -= 1
        else:
            j -= 1        
    return lcs
