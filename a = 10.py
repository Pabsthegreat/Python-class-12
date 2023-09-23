a = 10
def fun(b,c = 10):
    global a
    a = 5
    b = b + 10
    c = c + 10
    def fn():
        nonlocal a
        d = 11
    fn()
    print(a,b,c)
fun(10)
print(a)