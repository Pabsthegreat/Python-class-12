f = open(r'C:\Users\adars\OneDrive\Documents\PYTHON\Python class 12\Filehandling\Q5.txt','r')
g = open(r'C:\Users\adars\OneDrive\Documents\PYTHON\Python class 12\Filehandling\Q5.txt','a')
def fn():
    u = input('Enter username:')
    p = input('Enter password:')
    s = ' '
    while s:
        e = f.readline()
        if e == u + "," + p:
            print("Welcome ",u)
            break
        else:
            g = open(r'C:\Users\adars\OneDrive\Documents\PYTHON\Python class 12\Filehandling\Q5.txt','a')
            g.write("\n" + u + "," + p)
            break
            


while True:

    q = input("Dp you want to log in? (y/n):")
    if q == "y":
        fn()
        
    if q == "n":
        break
    
f.close()
g.close()