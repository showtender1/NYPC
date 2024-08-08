def t(A, B):
    boxes = min(A, B)
    big = max(A, B)

    if boxes * 3 < big:
        return -1

    total_sushi = A + B

    return (total_sushi + 3) // 4

n = int(input())
results = []

for _ in range(n):
    A, B = map(int, input().split())
    results.append(t(A, B))


for result in results:
    print(result)
