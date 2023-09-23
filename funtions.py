def op(x,y,z):
    if z == "+":
        a = x + y

    if z == "-":
        a = x - y

    if z == "*":
        a = x * y

    if z == "/":
        a = x / y

    return a


while True:
    q = input("Do you want to do a calculation?y/n:")

    while q not in ["y","n"]:
            print("Enter only y or n.")
            q = input("Enter only y or n only please:")

    if q == "y":
        
        x = input("Enter a number:")
        while x.isdigit() == False:
            print("Do not enter other characters than numbers.")
            x = input("Enter a number only please:")
        x = int(x)
            
        y = ("Enter a number:")
        while y.isdigit() == False :
            print("Do not enter other characters than numbers.")
            y = input("Enter a number only please:")
        y = int(y)

        z = input("Enter an operator:")
        while z not in ["+","-",'*',"/"]:
            print("Do not enter other characters than numbers.")
            z = input("Enter an operator only please:")

        if y == 0 and z == "/":
            print("Zero division error")
            break

        print(op(x,y,z))

    if q == "n":
        exit
#0 div
    
