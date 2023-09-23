x = True
while x == True:
    try:
            x = input("Enter a string:")

            if len(x) != 4:
                print("length has to be 4 characters")

            y = int(input("Enter a number:"))

            if len(x) == 4 and type(y) == int:
                x = False

            else:
                x = True

    except Exception as e:
        print(e)
        print("Please enter a number")
        x = True

    else:
        print("done")

    finally:
        print("moving on")
        
