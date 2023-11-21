def factx(n):
    if n == 0:
        return 1
    return n * factx(n-1)

def factx1(n):
    if n == 0:
        return 1
    out = factx(n-1)
    return n * out

def sum_n(n):
    if n <= 1: 
        return n 
    return n + sum_n(n - 1)

ent = int(input("Enter: "))
print(factx(ent))
print(sum_n(ent))