n = int(input("Enter number of elements :"))

l = [input("Enter an element:") for i in range(n)]

m = [i[::-1].capitalize() for i in l if type(i) != int]
print(m)
