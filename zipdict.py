set1 = ((1, 'Good', 2), (3, 'Luck', 4))
set2 = ['key', 'value', 'id']
li = []

for i in range (len(set1)):
    d = dict(zip(tuple(set2),set1[i]))
    li += [d]

print(li)
    
