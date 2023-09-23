#try except block
def do():
    try:
        x = int(input("y or n:"))
        if x == 1:
            print("fuck you")
        elif x == 2:
            print("fuck me")
    except:
        if TypeError:
            print("please enter an integer")
        do()
    else:
        print("yes")
    finally:
        print("your mom")

#linear search
def linearSearch(list, key): #function to perform the search
    for index in range(0,len(list)):
        if list[index] == key: #key is present
            return index + 1 #position of key in list
    return None #key is not in list

list1 = [] #Create an empty list
maximum = int(input("How many elements in your list? "))
print("Enter each element and press enter: ")
for i in range(0,maximum):
    n = int(input())
    list1.append(n) #append elements to the list
print("The List contents are:", list1)
key = int(input("Enter the number to be searched:"))
position = linearSearch(list1, key)
if position is None:
    print("Number",key,"is not present in the list")
else:
    print("Number",key,"is present at position",position)

#binary search

def binarySearch(list, key):
    first = 0
    last = len(list) - 1
    while(first <= last):
        mid = (first + last)//2
        if list[mid] == key:
            return mid
        elif key > list[mid]:
            first = mid + 1
        elif key < list[mid]:
            last = mid - 1
    return -1
list1 = [] #Create an empty list
print ("Create a list by entering elements in ascending order")
print ("press enter after each element, press -999 to stop")
num = int(input())
while num !=-999:
    list1.append(num)
    num = int(input())
n = int(input("Enter the key to be searched: "))
pos = binarySearch(list1,n)
if(pos != -1):
    print( n,"is found at position", pos+1)
else:
    print (n,"is not found in the list ")

#