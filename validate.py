import random
import re
def otp():
    OTP=random.randint(1000,9999)
    print(OTP,end="\n\n\n")
    IP()
def captcha():
    cap=input("Enter your captcha code: ")
    Dig,low,up,spec=False,False,False,False
    if len(cap)<4:
        print("Invalid captcha, too short",end="\n\n\n")
        captcha()
    for char in cap:
        if ord(char) >47 and ord(char)<58:
            Dig=True
        elif ord(char)>96 and ord (char)<123:
            low=True
        elif ord(char)>64 and ord(char)<91:
            up=True
        else:
            spec=True
    if Dig==True and low==True and up==True and spec==True:
        print("Valid captcha",end="\n\n\n")
        IP()
    else:
        print("Invalid captcha",end="\n\n\n")
        IP()
'''
def valid(email):
    regex=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{3,})+')
    if re.fullmatch(regex,email):
        print("Valid email",end="\n\n\n")
        IP()
    else:
        print("Invalid email",end="\n\n\n")
        IP()
'''
def IP():
    print("1. OTP generator\n2. Captcha verifier")
    choice=input("Enter your preferred option: ")
    if choice=='1':
        otp()
    elif choice=='2':
        captcha()
    else:
        print("Invalid option",end="\n\n\n")
        IP()
IP()
    
