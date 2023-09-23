f = open(r'C:\Users\adars\OneDrive\Documents\PYTHON\Python class 12\Filehandling\Q6.txt','r')
g = open(r'C:\Users\adars\OneDrive\Documents\PYTHON\Python class 12\Filehandling\guests.txt','w+')
h = open(r'C:\Users\adars\OneDrive\Documents\PYTHON\Python class 12\Filehandling\invitations.txt','w')
r = f.readlines()
t = r.copy()

def fn():
    global r
    n = int(input("Enter number of guests :"))
    g.seek(0)
    h.seek(0)
    for i in range(n):
        guests = input("Enter name of guest :")
        g.write(guests +"\n")

    for i in r:
        if i == "Dear Friend,\n" :
            g.seek(0)
            for f in range(n):
                r1 = g.readline()
                r1 = r1[:len(r1) - 1]
                t[r.index(i)] = "Dear " + r1 + "," + "\n"
                if f == 0:
                    t.append(r1 + "\n")
                else:
                    t.pop(-1)
                    t.append(r1 + "\n")
                   
                h.writelines(t)
                h.write("\n--------------------------------------------------------------------------------------------------------\n\n")

while True:
    q = input("Do you want to write invitations?(y/n) :")
    
    if q == "y":
        fn()
        
    if q == "n":
        break

f.close()
g.close()
h.close()    