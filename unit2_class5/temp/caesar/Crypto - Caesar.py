a = "GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT BS PNRFNE NAQ LBHE HAVDHR FBYHGVBA VF EQQNBFNOYECT"
for i in range(1, 26):
    list=[]
    for j in range(0, len(a)):
        if a[j]!=' ':
            list.append(chr(ord('A')+(ord(a[j])-ord('A')+i)%26))
        else:
            list.append(" ")
    print ''.join(list)  