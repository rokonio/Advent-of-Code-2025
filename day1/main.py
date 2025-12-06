content = open(0).read()

s = 0

dial = 50
for inst in content.splitlines():
    dir = 0
    if inst[0] == "R":
        dir += int(inst[1:])
    elif inst[0] == "L":
        dir -= int(inst[1:])
        # while dial <= 0:
        #     s += 1
        #     dial += 100
    else:
        assert False
    sign = 1 if dir > 0 else -1

    for n in range(0, dir, sign):
        dial += sign
        dial %= 100
        if dial == 0:
            s += 1
            print(f"At n={n}")
            # print("")
            # print(f"===={n}===")

print(s)
