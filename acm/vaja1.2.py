a = input("")
#a = "asdflkjasdlfj"


def beauty(n):
    x = 0
    shorter_words = 0
    longer_words = 0
    for i in n:
        if i == ' ' or i == ',' or  i == '!' or i == '?' or i == '.':
            if x > 8:
                longer_words += 1
            elif x < 3 and x > 0:
                shorter_words += 1
            x = 0
            continue
        x += 1

    if x > 8:
        longer_words += 1
    elif x < 3 and x > 0:
        shorter_words += 1
    
    if shorter_words == 0 and longer_words == 0:
        return 'Vse besede so znotraj predpisane dolžine'
    else:
        return "Predolgih besed je {} in prekrathih {}" .format(longer_words, shorter_words)

print(beauty(a))

