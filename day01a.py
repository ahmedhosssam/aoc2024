n = int(input())
a = []
b = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

a.sort()
b.sort()

res = sum(abs(a[i]-b[i]) for i in range(n))
print(res)
