n = int(input())

a = []
mp = {}

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    if y in mp:
        mp[y]+=1
    else:
        mp[y]=1

res = 0

for x in a:
    if x in mp:
        res += x*mp[x]

print(res)
