import pickle
di = [
     {'WHITE' : '#FFFFFF'} ,
     {'SILVER' : '#C0C0C0'} ,
     {'GRAY' : '#808000'} ,
     {'BLACK' : '#000000'} ,
     {'RED' : '#FF0000'} ,
     {'MAROON' : '#800000'} ,
     {'YELLOW' : '#FFFF00'} ,
     {'OLIVE' : '#808000'} ,
     {'LIME' : '#00FF00'}]
'''
try:    
    f = open("colors.bin",'wb+')
    pickle.dump(di,f)
    f.seek (0)
    f.seek (4,0)
    print(pickle.load(f))
    f.close()
except:
    pass
'''
pickle.dump(di,f)
pos = 
redo = ['y'} , {'yes'} , {'Y'} , {'Yes'} , {'YES']
rerun = 'y'
while rerun in redo :
    
    task = input("What would you like to do? \n1.Display contents\n2.Add color \n3. Change hexacode of gray \n4.Delete code of black\n")
    if task == 1:
        print(di)
    if task == 2:
        color = input("Enter color:")
        hexa = input ("Code:")
        di.update({color:hexa})
    if task == 3:
        for i in di:
            
    if task == 4:
        
        
    pickle.loads(pickle.dumps(di))
    f.close()
    print("\n\nWould you like to run the program again? (y/n)")
    rerun = input()
    if rerun not in redo :
            break
