def factx(n):
    if n == 0:
        return 1
    return n * factx(n-1)

def factx1(n):
    if n == 0:
        return 1
    out = factx(n-1)
    return n * out

ent = int(input("Enter: "))
print(factx1(ent))