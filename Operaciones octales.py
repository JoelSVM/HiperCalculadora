# -*- coding: cp1252 -*-
def Operaciones_Octales(bits,bits2,op):
    aList=[]
    bList=[]
    n=len(bits)
    h=len(bits2)
    valor=0
    valor2=0
    resultado=0
    conversion=""
    k=0
    c=0
    q=0
    w=0
    e=0
    for i in range(len(bits)):
        aList.append(8**(n-1))
        bList.append(8**(h-1))
        n-=1
        h-=1
        if i<len(bits):
            k=int(aList[i])
            c=int(bits[i])
            valor+=k*c
        
        if q<len(bits2):
            e=int(bList[q])
            w=int(bits2[q])
            valor2+=e*w
        q+=1

    if(op==1):
        resultado=valor+valor2
        
    if(op==2):
        resultado=valor-valor2
        
    if(op==3):
        resultado=valor*valor2
        
    if(op==4):
        resultado=valor//valor2
        
    while resultado // 2 != 0:
        conversion = str(resultado % 8) + conversion
        resultado = resultado // 8
            
    return str(resultado) + conversion

    
bits=raw_input('Dame un número octal: ')
bits2=raw_input('Dame un número octal: ')
op=int(input('Dame un número op 1 para +, 2 para -, 3 para *, 4 para /: '))

print 'Su valor decimal es',(Operaciones_Octales(bits,bits2,op))

