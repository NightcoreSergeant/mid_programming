def round_me(n):
    a = n - int(n)
    if n >= 0:
        return round(n)
    elif n < 0 and n >= -0.5:
        return '-0'
    
    elif a >= -0.5:
        return int(n)
    else:
        return int(n) - 1
    

b = float(input("> "))
print(round_me(b))