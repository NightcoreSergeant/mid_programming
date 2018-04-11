def compare(a, b):
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if a[i] != "?" and b[i] != "?" and a[i] != b[i]:
            return False
    return True

a = "abc?fg"
b = "ab?afg"

print(compare(a,b))