a,b,c = (5, 4, (8, (7, 8, 5),4))
d,e,f = c
g,h,i = e

l = [a,b,d,f,g,h,i]
d = {}

for i in l:
    x = l.count(i)
    d[i] = x

print(d)
