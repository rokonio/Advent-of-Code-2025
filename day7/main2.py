from functools import lru_cache
content = open(0).read()
grid = [list(line.strip()) for line in content.splitlines()]
s = 0

@lru_cache(maxsize=10_000)
def pathes(pos):
    tot = 0
    r, c = pos
    if r == len(grid)-1:
        return 1
    if not grid[r+1][c] == "^": 
        return pathes((r+1, c))
    if c > 0 and grid[r+1][c-1] == ".":
        tot += pathes((r+1, c-1))
    if c < len(grid[r])-1 and grid[r+1][c+1] == ".":
        tot += pathes((r+1, c+1))
    return tot

for c, char in enumerate(grid[0]):
    if char == "S": 
        s = pathes((0, c))

print(f"s = {s}")