
f = open("hi.txt","r")
l = ""
d = ''
u = ''
s = f.read()
s1 = ''
sp = 0
for i in s:
    if i.isupper():
        u += i
    if ord(i)>= 48 and ord(i) <= 57:
        d += i
    if i.islower():
        l += i
    if i == " ":
        sp += 1
        

s1 += s[::-1]
nl = s.count("\n")
print("spaces- ",nl - 1)
print(" caps - ",u)
print(" digits - ",d)
print(" lowercase - ",l)
f.close()

f1 = open("digit.txt","w")
f1.write(d)
f1.close()

f2 = open("lower.txt","w")
f2.write(l)
f2.close()

f3 = open("caps.txt","w")
f3.write(u)
f3.close()

f4 = open("rev.txt","w")
f4.write(s1)
f4.close()
    
    
