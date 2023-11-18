def factx(n):
    if n == 0:
        return 1
    return n * factx(n-1)

ent = int(input("Enter: "))
print(factx(ent))