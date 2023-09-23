f = open(r"Z:\C11BS94997\Class 12\Term 1\Q1file.txt","r")
s1 = ' '
s = [] 
s1 = f.readlines()
s1.reverse()
for i in s1:
    print(i)
