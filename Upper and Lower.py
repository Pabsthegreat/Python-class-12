f = open(r'Z:\C11BS10274\Class 12\Lab Week 4\Text files\L&T space.txt')
f1 = open(r'Z:\C11BS10274\Class 12\Lab Week 4\Text files\upper.txt','w')
f2 = open(r'Z:\C11BS10274\Class 12\Lab Week 4\Text files\lower.txt','w')
f3 = open(r'Z:\C11BS10274\Class 12\Lab Week 4\Text files\num.txt','w')
s= f.read()
f.close()
up = ''
low = ''
num = ''
for i in s:
    if i.isupper():
        up += i
    elif i.islower():
        low+= i
    elif i.isdigit():
        num+= i
f1.write(up)
f2.write(low)
f3.write(num)
f1.close()
f2.close()
f3.close()
