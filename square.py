def arp(x,y):
    ar = x*y
    per = 2*(x+y)
    return ar,per

q = input("Square or rectangle?")
if q == "rectangle":
    x = input("Enter a number:")
    while x.isdigit() == False:
        print("Do not enter other characters than numbers.")
        x = input("Enter a number only please:")
    x = int(x)
        
    y = ("Enter another number:")
    while y.isdigit() == False :
        print("Do not enter other characters than numbers.")
        y = input("Enter a number only please:")
    y = int(y)
    
    print(arp(x,y))

if q == "square":
    l = input("Enter a number:")
    while x.isdigit() == False:
        print("Do not enter other characters than numbers.")
        l = input("Enter a number only please:")
        
    l = int(l)
    
    def sq():
        arp(l,l)

    print(sq())

