from math import *
content = open(0).read().strip()
s = 0
loop = True

def croissant(t):
    for c in range(len(t)-1):
        if not ord(t[c]) == ord(t[c+1])-1:
            return False
    return True

for c in content.split(",")[:]:
    # if len(c) == 0:continue
    [idstart, idend] = c.split("-")
    start = int(idstart)
    end = int(idend)

    for i in range(start, end+1):
        text = str(i)
        for n in range(2, 12):
            if len(text)%n != 0:
                continue
            l = len(text) // n
            # if not croissant(text[:l]): continue
            l0 = text[:l]
            ok = True
            for part in range(1, n):
                if text[part*l:(part+1)*l] != l0:
                    ok = False
                    break
            if ok:
                s += i
                break

        

# 1: 40214376723
#2: 50793864718

#rank 2, 2386
print(s)