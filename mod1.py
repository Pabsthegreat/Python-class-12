import random

def otp():
    x = ""
    for i in range(4):
        x += str(random.randint(0,9))

    return int(x)

def up():
    x = random.randint(65,90)
    return chr(x)
     

def sp():
    y = random.randint(33,47)
    return chr(y)

def lw():
    z = random.randint(97,122)
    return chr(z)

def di():
    a = random.randint(0,9)
    return str((a))  

def capt(x = 4):

    capt = ""
    if x < 4:
        x = 4

    if x > 4:
        i = x - 4

        for i in range(i):
            m = random.choice(["x","y","z","a"])
            if m == "x":
                capt += up()

            if m == "y":
                capt += sp()

            if m == "z":
                capt += lw()

            if m == "a":
                capt += di()
                
    capt += sp()+lw()+di()+up()
        

capt()
otp()


def email(x):
    if "@" not in x :
        return "invalid"

    
    
