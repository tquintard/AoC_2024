from functools import cmp_to_key
from common import get_input

inputs = get_input(5, "", False)


rules, pages = inputs.split('\n\n')
cmp = cmp_to_key(lambda x, y: -(x+'|'+y in rules))

a = [0, 0]
for p in pages.split():
    p = p.split(',')
    s = sorted(p, key=cmp)
    a[p != s] += int(s[len(s)//2])

print(*a)
