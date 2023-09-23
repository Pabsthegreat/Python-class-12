#Bubble sort
data = []
n = int(input('Enter number of elements in unsorted list '))
for i in range(n):
    ele = int(input('Enter element ' + str(i) + ' ')) 
    #indicate which element needs to be entered
    data += [ele]
#Display the list
print ('You entered:')
for i in data:
    print (i, end = ' ')
print()


#begin sort
for i in range(n-1):
    for j in range(0,n-1-i):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]

#display sorted list
print('list after sorting ')
for i in data:
    print (i, end = ' ')



'''
Real World Applications of Sorting:

Bubble Sort:
Bubble sort is used in programming TV remote to sort channels on
the basis of longer viewing time.


Insertion sort:
a)The contact list in your phone is sorted, which means you can easily access
your desired contact from your phone since the data is arranged in that
manner for you. 

b)While shopping on flipkart or amazon, you sort items
based on your choice, that is, price low to high or high to low.



Merge Sort:
Databases use an external merge sort to sort sets of data
that are too large to be loaded entirely into memory.
The driving factor in this sort is the reduction in the number of disk I/Os.



Heap Sort: Heap sort is used in reading barcodes on plastic cards.
The service allows to communicate with the database to constantly
run checks to ensure that they were all still online and had to
constantly report statistics on which readers were performing the worst,
which ones got the most/least user activity, etc.


Quick Sort: Sports scores are organised by quick sort on the basis of win-loss ratio.


Radix Sort: eBay allows you to sort listings by the current Bid
amount leveraging radix sort.


Selection Sort: Education portal allows sorting list of
pupils alphabetically through selection sort.

'''