import pickle
def read_c():
    try:
        with open("countries.dat",'rb') as f:
            while True:
                lst = pickle.load(f)
        
    except:
        pass
    couci = input("Enter country or city:")
    for i in lst:
        if i[0] or i[1] ==couci.title():
            print(i)
read_c()

    
