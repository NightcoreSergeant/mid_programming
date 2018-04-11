def emso(a):
    return "{}.{}.{}".format(a[:2:1], a[2:4:1], "2" + a[4:7])


print(emso("12222222222"))