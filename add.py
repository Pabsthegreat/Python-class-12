t1 = (2, 10, 15, 5)
t2 = (8, 7, 20, 11)
l = tuple(t1[i]+t2[i] for i in range(len(t1)))
print(l)
