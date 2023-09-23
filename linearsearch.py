def linear_Search(list1,element):  
    for i in range(0, len(list1)):  # Searching list1 sequentially  
        if (list1[i] == element):  
            return i  
    return -1  
    
list1 = [1 ,13, 75, 4, 7, 99]  
item = 7  
  
res = linear_Search(list1,item)  

if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at: ", (res+1),"position")  