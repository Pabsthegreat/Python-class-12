matrix = ()
sum = 0
for i in range(1,4):
    print("Now enter values for row",i)
    t = ()
    for j in range(3):
        x = int(input("Enter a number:"))
        t += (x,)
        if x % 2 == 0:
            sum += x
    matrix += (t,)

print("The matrix is :",matrix)
print("Sum of even numbers = ",sum)
