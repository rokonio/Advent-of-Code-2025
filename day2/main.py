from math import *
content = open(0).read().strip()
s = 0
loop = True

for c in content.split(",")[:]:
    # if len(c) == 0:continue
    [idstart, idend] = c.split("-")
    ms = (len(idstart))//2
    me = (len(idend)+1)//2

    if ms <= 0:
        start = int(idstart)
    else:
        start = int(idstart[:ms])
    
    if me <= 0:
        end = int(idend)
    else:
        end = int(idend[:me])

    realstart = int(idstart)
    realend = int(idend)

    print(realstart, realend)
    print(start, end)
    for a in range(start, end+1):
        # print(a)
        # n = a*(1 + 10**int(log10(a)+1))
        n = int(str(a)+str(a))
        print("   ", n)
        if realstart <= n <= realend:
            s += n
            print(" => ", n)
        if n > realend:
            break
    print()

print(s)