def compare(a, b):
    x = 0
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if (a[i] == "?" or b[i] == "?") or (a[i] == b[i]):
            x += 1
        if x == len(a):
            return True
    return False

a = "abc?fg"
b = "abmafg"

print(compare(a,b))