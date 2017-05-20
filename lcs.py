import sys


def lcs(s1, i, s2, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + lcs(s1, i + 1, s2, j + 1)
    else:
        return max(lcs(s1, i + 1, s2, j), lcs(s1, i, s2, j + 1))


def lcs_opt(s1, s2):
    m = len(s1)
    n = len(s2)
    f = list()
    # inner_f = list()
    f.append([0 for i in range(0,m+1)])
    for j in range(0,n):
        f.append([0 if i is 0 else None for i in xrange(0,m+1)])
    for i in xrange(1, n + 1, 1):
        for j in xrange(1, m + 1, 1):
            if s1[j - 1] == s2[i - 1]:
                # print(i,j,f[i][j])
                f[i][j] = f[i-1][j-1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    # print(f)
    return f[n][m]


def lcs_recur_opt(s1, i, s2, j):
    if f[i][j] is not None:
        return f[i][j]
    if i == c or j == r:
        f[i][j] = 0
    elif s1[i] == s2[j]:
        f[i][j] = 1 + lcs_recur_opt(s1, i + 1, s2, j + 1)
    else:
        f[i][j] = max(lcs_recur_opt(s1, i + 1, s2, j),
                      lcs_recur_opt(s1, i, s2, j + 1))
    return f[0][0]


if __name__ == '__main__':
    # s1 = raw_input()
    # s2 = raw_input()
    s1 = "abcdafaab"
    s2 = "acafab"
    r = len(s2)
    c = len(s1)
    f = [[None] * (c + 1)] * (r + 1)
    # print(f)
    # print(lcs_recur_opt(s1, 0, s2, 0))
    print(lcs(s1,0,s2,0))
    print(lcs_opt(s1,s2))
