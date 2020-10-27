a = 1
while a < 10:
    b = 1
    while b <= a:
        print("%dx%d=%d\t" %(b, a, a*b), end="")
        b = b + 1
    print("")
    a = a + 1
