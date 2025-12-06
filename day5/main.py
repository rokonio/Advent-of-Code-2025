content = open(0).read()
grid = content.splitlines()
s = 0

ranges, fresh = content.split("\n\n")
set_r = list()
for line in ranges.splitlines():
    left, right = line.split("-")
    left = int(left)
    right = int(right)
    set_r.append([left, right+1])

set_r.sort()
print(set_r)

for r in range(len(set_r)-1):
    (l1, r1) = set_r[r]
    (l2, r2) = set_r[r+1]
    set_r[r+1][0] = max(min(r1, r2), l2)

print(set_r)
for (l, r) in set_r:
    s += r - l

print(f"s = {s}")
# Two parts: 27 mins