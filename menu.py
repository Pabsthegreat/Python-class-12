while True:

    q = input("Do you want to start?(y/n):")
    while q.lower() not in ["y","n"]:
        print("Enter y or n")
        q = input("Do you want to start?(y/n):")

    if q.lower() == "n":
        break

    x = input("Enter a string:")
    
    print("What do you want to do?:\na.count number of capital letters, vowels, numbers and special characters.\
    \nb.check whether the string is palindrome or not.")

    y = input("Enter option:")
    while y.lower() not in ["a","b"]:
        print("Enter a or b")
        y = input("Enter option:")

    if y.lower() == "a":
        cap = 0
        v = 0
        num = 0
        sp = 0
        for i in x:
            if i.isupper():
                cap += 1
            if i.isdigit():
                num += 1
            if i.isalnum() == False:
                sp += 1
            if i.upper() in "AEIOU":
                v += 1
        print("Number of capital letters are:",cap,"\nNumber of vowels are:",v,\
            "\nNumber of numbers are:",num,"\nNumber of special characters are:",sp)

    if y.lower() == "b":
        xalt = ""
        for i in x:
            xalt = i + xalt
        if xalt == x:
            print(x,"Is a palindrome.")




        

    





