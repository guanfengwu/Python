a = int(input('请输入层数：'))

for i in range(a):
                                        
    print('   '* (a-i), end='')

    j = i+1
    while j != 0:
        print(format(j,"3d"), end='')
        j = j - 1

    m=2
    while m != i+2:
        print(format(m,"3d"), end='')
        m = m + 1
    print()
