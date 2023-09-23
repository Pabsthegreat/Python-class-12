#3x3 matrix
tup1 = ()
sue = 0
for i in range(3):
    tup = ()
    for j in range (3):
        x = int(input("Enter numbers"))
        tup += (x,)
        if x % 2 == 0:
            sue += x
    tup1 += (tup,)

print(sue)
print(tup1)


    
