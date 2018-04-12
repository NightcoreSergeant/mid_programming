def common(a, b):
    max_a = 0
    max_str = None
    for i in a:
        x = i.count("{}".format(b))
        if x > max_a:
            max_a, max_str = x, i
    return "{} => {}".format(max_str,max_a)





l = ["aavdasa","asdfvv","asdfaaaasdbaa","adfiieea"]
a = "a"
print(common(l, a))