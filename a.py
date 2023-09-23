x = 10
def fn(l = x, m = []):
    m.append(l)
    print(m)
x = 20
n = [1]
fn(m = n)
print(n)