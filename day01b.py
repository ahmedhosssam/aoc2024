n = int(input())
a = []
mp = {}

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    if y not in mp: mp[y]=0 
    mp[y]+=1

res = sum(x*mp[x] if x in mp else 0 for x in a)

print(res)
