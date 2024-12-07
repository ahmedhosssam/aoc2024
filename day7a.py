N = int(input())

res = 0

for _ in range(N):
    a = input()
    a = list(a.split(' '))
    target = int(a[0][:-1])
    del a[0]
    a = [int(x) for x in a]
    n = len(a)-1
    for b in range(2**n):
        arr = []
        for i in range(n):
            arr.append('+') if b&(2**i) else arr.append('*')
        g = []
        for i in range(n):
            g.append(a[i])
            g.append(arr[i])
        g.append(a[len(a)-1])

        print(g)
        i = 0
        while i < len(g):
            if g[i] == '*':
                if i > 0 and i + 1 < len(g):
                    g[i-1] = g[i-1] * g[i+1]
                    del g[i+1]
                    del g[i]
                    i -= 1
            else:
                i += 1
        i = 0
        print(g)
        while i < len(g):
            if g[i] == '+':
                if i > 0 and i + 1 < len(g):
                    g[i-1] = g[i-1] + g[i+1]
                    del g[i+1]
                    del g[i]
                    i -= 1 
            else:
                i += 1
        
        print(g)
        if g[0] == target:
            res += g[0]
            print(target)

print(res)

'''
12 + 131 * 67 * 45
'''
