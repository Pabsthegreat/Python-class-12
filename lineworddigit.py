f = open("filenames.txt","r")
st = ' '
def fn(y):
    global m
    l = 0
    d = 0
    s = y.read()
    for i in s:
        if i == "\n":
            l += 1
        if ord(i)>= 48 and ord(i) <= 57:
            d += 1
    w = s.split()
    print(m,"\nno. of lines = ",l,"\nno.of words = ",len(w),"\nno. of digits = ",d)

while st:
    st = f.readline()
    if st[-1] != "\n":
        m = st[:len(st)]
    else:
        m = st[:len(st)-1]
        
    x = open(m,"r")
    fn(x)

