n, m = map(int, input().split())

a = []
valid = [] # the name should be not valid this time

for _ in range(n):
    s = input()
    s = list(map(int, s.split('|')))
    a.append(s)

g = input() # to skip empty line

for _ in range(m):
    s = input()
    s = list(map(int, s.split(',')))
    ok = 1
    for x in a:
        I = -1
        J = -1
        if x[0] in s and x[1] in s:
            for j in range(len(s)):
                if s[j]==x[0]: I=j
                if s[j]==x[1]: J=j
        if I>J: ok=0; break
    if not ok: valid.append(s)

res = 0

for i, y in enumerate(valid):
    first = []
    second = []
    for x in a:
        if x[0] in y and x[0] not in second:
            first.append(x[0])
        if x[1] in y and x[1] not in first:
            second.append(x[1])
    valid[i] = first + second

for x in valid:
    res += x[len(x)//2]

print(res)
