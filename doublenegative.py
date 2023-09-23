x = int(input("Enter number :"))
l = [i*2 if i % 2 == 0 else -i for i in range(x +1)]
print(l)
