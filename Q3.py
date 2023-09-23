import re

def email(e):
    e = str(e)
    for i in e:
        if i.isalnum() == False and i not in ["@",".","-","_"]:
            print("Invalid Email!")
            break


    if "@" not in e:
        print("invalid email!")

    else:
        i = e.index("@")

        if " " in e[:i] or e[i:].count(".") > 2 or e[i:].count(".") < 1:
            print("Invalid email!")

        else:
            if  e[i:].count(".") == 1:
                j = e[i:].index(".")

                if len(e[i:][j+1:]) != 3:
                    print("iNvalid email!")
                else:
                    print("valid email !")

            elif e[i:].count(".") == 2:
                j = e[::-1].index(".")

                if len(e[:j]) != 2:
                    print("invAlid email!")
                else:
                    print("valid email !")

q = input("Enter email : ")
email(q)
