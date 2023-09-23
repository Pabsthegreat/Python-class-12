def FindPos(AR,item):
            size=len(AR)
            if item<AR[0]:                         # 
                return 0
            else:
                pos=-1                              #    
            for i in range(size-1):           
                if(AR[i]<=item and item<AR[i+1]):    #
                    pos=i+1                          #  
                    break
            if(pos==-1 and i<=size-1):               #
                pos=size
            return pos

def shift(AR,pos):
    AR.append(None)                   #[10, 20, 30, 50, 60, 70, None]
    size=len(AR)

    i=size-1                           #i=6
    while i>=pos:                      #6>=4
        AR[i]=AR[i-1]                  #[10, 20, 30, 50, 50, 60, 70]
        i=i-1

#main
lst=[10,20,30,50,60,70]
item=40
position=FindPos(lst,item)
shift(lst,position)
lst[position]=item
print(lst)