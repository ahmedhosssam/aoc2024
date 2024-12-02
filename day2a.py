n = int(input())

# Only increasing or decreasing
# 1 <= abs(a[i]-a[i+1]) <= 3

res = 0

for _ in range(n):
    a = list(map(int, input().split()))
    x = True
    s = 'inc'
    for i in range(len(a)):
        if i==0 or a[i]==a[0]: continue
        if a[i] < a[0]: s = 'dec'; break
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1]) < 1 or abs(a[i]-a[i+1]) > 3: x = False
        if (a[i]>a[i+1] and s == 'inc') or (a[i]<a[i+1] and s == 'dec'): x = False
    if x: res += 1

print(res)
