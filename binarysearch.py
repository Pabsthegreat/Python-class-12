alist=[45,67,89,102,150]
first = 0
last = len(alist)-1
found = False
item=150

while first<=last and not found:
    midpoint = (first + last)//2
    if alist[midpoint] == item:
        found = True
    else:
        if item < alist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1

if found== True:
    print("Element found at ",midpoint+1)
else:
    print("Element not found")