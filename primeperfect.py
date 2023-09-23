import math

def isPrime(x):
    y = True
    for i in range(2,int(math.sqrt(x))):
        if int(math.sqrt(x)) % i == 0:
            y = False
            break
        else:
            y = True
            
    print(y)

isPrime(78)

