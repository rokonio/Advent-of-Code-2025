content = [list(map(int, line.strip())) for line in open(0)]
s = 0

for bank in content:
    res=bank[:]
    digits = []
    for n in reversed(range(1, 12)):
        first = max(res[:-n])
        pos = res[:-n].index(first)
        res = res[pos+1:]
        digits += [first]
    digits += [max(res)]
    s += int("".join(map(str, digits)))
    
# Time: 18 mins (part 1 and 2)

print(s)