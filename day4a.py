n, m = map(int, input().split())
grid = []

for _ in range(n):
    s = input()
    grid.append(s)

def count_xmas_occurrences(grid):
    def is_within_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def count_word_from(x, y, dx, dy):
        count = 0
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_within_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return 0
        return 1

    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    total_count = 0

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                total_count += count_word_from(x, y, dx, dy)

    return total_count

res = count_xmas_occurrences(grid)

print(res)
