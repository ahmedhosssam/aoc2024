n, m = map(int, input().split())

a = []
valid = []

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
    if ok: valid.append(s)

res = 0

for x in valid:
    res += x[len(x)//2]

print(res)
