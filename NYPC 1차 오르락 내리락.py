def k(n, arr):
    def k(start, end):
        odd = arr[start:end + 1:2]
        even = arr[start + 1:end + 1:2]
        return all(odd[i] < odd[i + 1] for i in range(len(odd) - 1)) and all(
            even[i] > even[i + 1] for i in range(len(even) - 1))

    max_length = 0
    for start in range(n):
        for end in range(start, n):
            if k(start, end):
                max_length = max(max_length, end - start + 1)
    return max_length


n = int(input())
arr = list(map(int, input().split()))

print(k(n, arr))
# 테스트케이스 1번만 통과되는 wwww
