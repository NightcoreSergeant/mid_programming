a = ''' V  Notranjem stoji vas, Vrh po imenu. V tej vasici je ˇzivel
v starih ˇcasih Krpan, moˇcan in silen ˇclovek. Bil je neki
tolik, da ga ni kmalu takega. Dela mu ni bilo mar; ampak nosil
je od morja na svoji kobilici angleˇsko sol, kar je bilo
pa ˇze tistikrat ostro prepovedano. '''



def average_sign(txt, letter):
    a = []
    celotno = []
    line = 1
    x = 1
    for b in txt:
        if b == letter:
            a.append(x)
            celotno.append(x)
        elif b == '\n':      
            line += 1
            x = 0
            if len(a) != 0:
                print("v {} vrstici: {}".format(line, sum(a)//len(a)))
            else:
                print("v {} vrstici: 0".format(line))
            a = []
        x += 1
    print("v {} vrstici: {}".format(line, sum(a)//len(a)))
    return 'v celotnem je: {}'.format(sum(celotno)//len(celotno))
k = 'k'
print(average_sign(a, k))






















#"v prvi vrstici:{}\nv drugi vrstici:{}\nv tretji vrstici:{}\nv cetrti vrstici:{}\nv peti vrstici:{}\nv celotnem besedilu:{}".forat()    