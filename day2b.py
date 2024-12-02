n = int(input())

# Only increasing or decreasing
# 1 <= abs(a[i]-a[i+1]) <= 3
'''
To count additional reports to be safe:
We can count the number of elements that: (1) a[i-1] >= a[i] <= a[i+1]  (2) a[i-1] <= a[i] >= a[i+1]  (3) 1 > abs(a[i]) > 3
'''

res = 0

for _ in range(n):
    a = list(map(int, input().split()))
    x = True
    s = ''
    inc = 0
    dec = 0
    for i in range(len(a)-1):
        if a[i]<a[i+1]: inc += 1
        if a[i]>a[i+1]: dec += 1
    if inc > dec: s = 'inc'
    elif dec > inc: s = 'dec'
    else: continue
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1]) < 1 or abs(a[i]-a[i+1]) > 3: x = False
        if (a[i]>a[i+1] and s == 'inc') or (a[i]<a[i+1] and s == 'dec'): x = False
    if x: res += 1
    else:
        for j in range(len(a)):
            b = list(a)
            del b[j]
            x = True
            for i in range(len(b)-1):
                if abs(b[i]-b[i+1]) < 1 or abs(b[i]-b[i+1]) > 3: x = False
                if (b[i]>b[i+1] and s == 'inc') or (b[i]<b[i+1] and s == 'dec'): x = False
            if x: res += 1; break 

print(res)
