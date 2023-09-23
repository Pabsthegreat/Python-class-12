n = int(input("Enter number of elements :"))
l = [int(input("Enter an element:")) for i in range(n)]
m = [str(i) for i in l if i % 5 == 0]
print(m)