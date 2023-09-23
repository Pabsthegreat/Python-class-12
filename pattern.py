def pat(x = 3):
    for i in range(1,x+1):
        for j in range(i):
            print("*",end = "")
        print()
try:            
    x = int(input("Enter a number for the pattern:"))
except:
    pat()
else:
    pat(x)
