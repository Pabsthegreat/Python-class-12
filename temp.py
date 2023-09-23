x = [34.3, 33.6, 32.7, 23.0]
def fn(x):
    for i in x:
        if i < 33.5:
            x.remove(i)
    print(x)

fn(x)
