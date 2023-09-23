def insertion_sort(lst):
    length = len(lst)
    for i in range(1,length):
        temp = lst[i]
        j = i-1
        while j >= 0 and temp < lst[ j ]:
            lst[j+1] = lst[j]
            j = j-1
        else :
            lst[j+1] = temp
    print(lst)

#lst = eval(input("Enter a String list = "))
#lst=['python','computer','express', 'games', 'portal']
lst=[225,784,584,124,345]
insertion_sort(lst)