
# -*- coding: cp1252 -*-
def Hexadecimal_decimal(bits):
    binadicth = {"a" : "10","b" : "11","c" : "12","d" : "13","e" : "14","f" : "15"}
    aList=[]
    n=len(bits)
    valor=0
    k=0
    c=0
    for i in range(len(bits)):
        aList.append(16**(n-1))
        n -=1
        k=int(aList[i])
        if bits[i] in binadicth:
            j=bits[i]
            c=int(binadicth.get(j))
        else:
            c=int(bits[i])
        valor+=k*c
    
    return valor

    
bits=raw_input('Dame un n�mero hexadecimal: ')  
print 'Su valor decimal es',(Hexadecimal_decimal(bits))



