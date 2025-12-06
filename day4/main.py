content = [list(row) for row in open(0).read().splitlines()]
s = 0

nrow = len(content)
ncol = len(content[0])

def remove():
    global content

    to_rem = set()
    for (r, row) in enumerate(content):
        for (c, col) in enumerate(row):
            if col != "@": continue
            adj = 0
            for (rrow, rcol) in [ (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
                if not (0 <= rrow < nrow and 0 <= rcol < ncol):
                    continue
                obj = content[rrow][rcol]
                if obj == "@":
                    adj += 1
                else:
                    assert obj == "."
            if adj < 4:
                to_rem.add((r, c))
    for (r, c) in to_rem:
        content[r][c] = "."
    return len(to_rem)
    #         print("x", end="")
    #     else:
    #         print(".", end="")
    # print()

def show():
    print(f"removed {last_rem}")
    for row in content:
        for col in row:
            print(col, end = "")
        print()

last_rem = remove()
while last_rem > 0:
    s += last_rem
    last_rem = remove()

# 18 mins

print(f"s = {s}")