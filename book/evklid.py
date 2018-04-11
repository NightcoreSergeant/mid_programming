def evklid(a, b):
    arg_max = max(a, b)
    arg_min = min(a, b)
    ost = arg_max % arg_min
    if ost == 0:
        return arg_min

    while ost != 0:
        if arg_max % arg_min == 0:
            break
        ost = arg_max % arg_min
        arg_max //= arg_min
        arg_max = arg_min
        arg_min = ost
        
    return ost

#print(evklid(1, 25))

def evk(a, b):
    while 0 < b:
        a, b = b, a % b
    return a

print(evk(0,25))
