def t(A, B):
    boxes = min(A, B)
    big = max(A, B)

    if boxes * 4 < big:
        return -1

    if big % 4 == 0:
        tmp = big // 4
    else:
        tmp = big // 4 + 1

    return tmp

n = int(input())
results = []

for _ in range(n):
    A, B = map(int, input().split())
    results.append(t(A, B))


for result in results:
    print(result)
