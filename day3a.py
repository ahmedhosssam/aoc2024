s = input()
res = 0
mul = ''

for i in range(len(s)):
    if s[i:i+3] == 'mul':
        mul += s[i:i+3]
        if s[i+3] == '(':
            mul += s[i+3]
            num1 = ''
            j = i+4
            while s[j].isdigit():
                num1 += s[j]
                j+=1
            if len(num1) > 3: continue
            else:
                mul += num1
                num1 = int(num1)
                i = j
                if s[i] == ',':
                    mul += s[i]
                    num2 = ''
                    j = i+1
                    while s[j].isdigit():
                        num2 += s[j]
                        j+=1
                    mul += num2
                    if s[j] == ')':
                        mul += s[j]
                        print(mul)
                        num2 = int(num2)
                        res += num1 * num2
    mul = ''

print(res)
