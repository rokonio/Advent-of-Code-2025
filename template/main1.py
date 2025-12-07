from functools import lru_cache
from collections import deque
content = open(0).read()
grid = [line.strip() for line in content.splitlines()]
s = 0


print(f"s = {s}")