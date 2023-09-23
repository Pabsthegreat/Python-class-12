import math
x = input("Enter a number:")
while x.isdigit() == False:
    print("Do not enter other characters than numbers.")
    x = input("Enter a number only please:")
x = int(x)
    
y = input("Enter lower limit of range:")
while y.isdigit() == False :
    print("Do not enter other characters than numbers.")
    y = input("Enter lower limit of range:")
y = int(y)

z = input("Enter upper limit of range:")
while z.isdigit() == False :
    print("Do not enter other characters than numbers.")
    z = input("Enter upper limit of range:")
z = int(z)

n = int(math.sqrt(z))
pri = []
perf = []
def isPrime(m):
    global pri
    t = True
    for i in range(2,m):
        if m % i == 0:
            t = False
            break
        else:
            t = True
    if t == True:
        pri += [m]

    return t

def isPerfect(n):
    global perf
    o = []
    for i in range(1,n):
        if n % i == 0:
            o += [i]
    if sum(o) == n:
        perf += [n]
        return True
    else:
        return False
    
for i in range (y,z+1):
    isPrime(i)
    isPerfect(i)

print("All prime numbers in the given range is:",pri)
print("All perfect numbers in the given range is:",perf)
print(x," a Prime?:",isPrime(x))
print(x,"a Perfect number?:",isPerfect(x))


            
        
