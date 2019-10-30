def highest_score(friends):
    n = len(friends)
    cnt = [0] * n
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            if friends[i][j] == 'Y':
                cnt[i] += 1
            else:
                for k in range(0, n):
                    if friends[i][k] == 'Y' and friends[j][k] == 'Y':
                        cnt[i] += 1
                


    return max(cnt)


# Example 0
# friends = ['NNN', 'NNN', 'NNN']

# Example 1
# friends = ['NYY', 'YNY', 'YYN']

# Example 2
friends = ['NYNNN', 'YNYNN', 'NYNYN', 'NNYNY', 'NNNYN']

print(highest_score(friends))
