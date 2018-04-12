def compare(a, b):
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if a[i] != "?" and b[i] != "?" and a[i] != b[i]:
            return False
    return True

a = "aaaaaaaaa?"
b = "aaaaaaaaaasdflasldfja"

#print(compare(a,b))

def priblizek(a, b):
    x = 0
    for i in range(min(len(a),len(b))):
        if a[i] == b[i]:
            x += 1
    
    if x < max(len(a),len(b)) * 0.9:
        return False
    else:
        return True

print(priblizek(a,b))