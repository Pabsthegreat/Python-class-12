def con(x):
    s = 0
    t = ""
    for i in x:
        if type(i) == int or type(i) == float:
            s += i

        if type(i) == str:
            t += i

    print("sum of ints = ",s,"\nstrings = ",t)
            
def con1(x):
    s = 1
    for i in x:
        
        if type(i) == int or type(i) == float:
            s *= i
    print("products of ints = ",s)
            
def fn():
    x = []
    try:
        num1=int(input("number of parameters:"))
        for i in range (num1):
            input1=eval(input("Enter the parameter :"))
            if type(input1) == int or type(input1) == float or type(input1) == str:
                x.append(input1)

    except ValueError:
        print("enter value again")
        fn()

    con(x)
    con1(x)

fn()      

        
    
    
