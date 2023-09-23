import random
def otp():
    ot = ''
    for i in range(4):
       ot += str(random.randint(0,9))
    print("Your OTP is : ",ot)

otp()
    