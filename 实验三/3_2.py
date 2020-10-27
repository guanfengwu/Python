tel = input()
tel = tel.upper()


for i in range(0,len(tel)):
    if tel[i]=='A' or tel[i]=='B' or tel[i]=='C':
        tel.replace(tel[i],"2")
    elif tel[i]=='D' or tel[i]=='E' or tel[i]=='F':
         tel.replace(tel[i],"3")
    elif tel[i]=='G' or tel[i]=='H' or tel[i]=='I':
         tel.replace(tel[i],"4")
    elif tel[i]=='J' or tel[i]=='K' or tel[i]=='L':
         tel.replace(tel[i],'5')
    elif tel[i]=='M' or tel[i]=='N' or tel[i]=='O':
         tel.replace(tel[i],'6')
    elif tel[i]=='P' or tel[i]=='Q' or tel[i]=='R' or tel[i]=='S':
         tel.replace(tel[i],'7')
    elif tel[i]=='T' or tel[i]=='U' or tel[i]=='V' :
         tel.replace(tel[i],'8')
    elif tel[i]=='W' or tel[i]=='X' or tel[i]=='Y' or tel[i]=='Z':
         tel.replace(tel[i],'9')
    print(tel)
        
