def count_exploding_lines(N, coordinates):
    from collections import defaultdict

    x_coords = defaultdict(int)
    y_coords = defaultdict(int)

    for x, y in coordinates:
        x_coords[x] += 1
        y_coords[y] += 1

    vertical_lines = sum(1 for count in x_coords.values() if count > 1)
    horizontal_lines = sum(1 for count in y_coords.values() if count > 1)

    return vertical_lines + horizontal_lines


N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

result = count_exploding_lines(N, coordinates)
print(result)
