def s(n):
    sq=n*n
    print(sq)
    return sq

def gen():
    yield s(2)
    yield s(3)
    return s(4)

for num in gen():
    print(num, end='-')
