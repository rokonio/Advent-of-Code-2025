grid = [line[:-1] for line in open(0)]
s = 0

for start in range(len(grid[-1])):
    op = grid[-1][start]
    if op == " ": 
        continue
    end = start + 1
    while end < len(grid[-1]) and grid[-1][end] == " ":
        end += 1
    acc = ["".join([row[nscol] for row in grid[:-1]]) for nscol in range(start, end)]
    acc = [int(n) for n in acc if n.strip() != ""]

    if op == "+":
        tot = sum(acc)
    elif op == "*":
        tot = 1
        for n in acc: tot *= n
    else:
        raise RuntimeError(op)
    print(f"tot = {tot}")
    s += tot

print(f"s = {s}")