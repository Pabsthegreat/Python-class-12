l = {'Box1': (400,200), 'Box2': (240,120)}
def fn(x):
    d = x
    for i in d:
        s = 0
        s = d[i][0]/d[i][1]
        d[i] = s

    print(d)    

x = {}
for i in range(5):
    try:
        for i in range(5):
            t = tuple(input("Enter tuple of  mass, volume"))
            x["Box"+str(i)] = t
    except Exception as e:
        if e == ValueError:
            t = tuple(input("Enter tuple of  mass, volume"))
        

        
        
        
    
