tel = input()
tel = tel.upper()
a=tel.split('-')
print(a)
for x in a:
    print(x)
    for y in x:
        print(y)
        if y=='A' or y=='B' or y=='C':
            y=1
        elif y=='D' or y=='E' or y=='F':
            x.replace(y,"3")
            
        elif y=='G' or y=='H' or y=='I':
            x.replace(y,"4")
        elif y=='J' or y=='K' or y=='L':
            x.replace(y,"5")
        elif y=='M' or y=='N' or y=='O':
            x.replace(y,"6")
        elif y=='P' or y=='Q' or y=='R' or y=='S':
            x.replace(y,"7")
        elif y=='T' or y=='U' or y=='V' :
            x.replace(y,"8")
        elif y=='W' or y=='X' or y=='Y' or y=='Z':
            x.replace(y,"9")
    print(x + "---")
        
