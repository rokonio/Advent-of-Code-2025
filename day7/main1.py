content = open(0).read()
grid = [list(line.strip()) for line in content.splitlines()]
s = 0

for c, char in enumerate(grid[0]):
    if char == "S": grid[0][c] = "|"

def step(r):
    global grid
    tot = 0
    for c, char in enumerate(grid[r]):
        if char != "|": continue
        if grid[r+1][c] == ".": grid[r+1][c] = "|"
        elif grid[r+1][c] == "^": 
            add = 0
            if c > 0 and grid[r+1][c-1] == ".":
                grid[r+1][c-1] = "|"
                add += 1
            if c < len(grid[r])-1 and grid[r+1][c+1] == "." and grid[r][c+1] != "|":
                grid[r+1][c+1] = "|"
                add += 1
            tot += 1
    # for c1, c2 in grid[r].zip(grid[r+1]):
    #     if c2 == "|" and c1 != "|":
    #         tot += 1
    print("Grid")
    # for line in grid:
    #     print("".join(line))
    print(f"tot = {tot}")
    return tot

for r, row in enumerate(grid):
    if r == len(grid)-1: continue
    s += step(r)

print(f"s = {s}")