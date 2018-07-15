def Operaciones_Hexadecimal(bits,bist2,op):
    binadicth = {"a" : "10","b" : "11","c" : "12","d" : "13","e" : "14","f" : "15"}
    binadicths = {"10" : "a","11" : "b","12" : "c","13" : "d","14" : "e","15" : "f"}
    aList=[]
    bList=[]
    xList=[]
    n=len(bits)
    f=len(bits2)
    valor=0
    valor2=0
    conversion=""
    k=0
    l=0
    c=0
    y=0
    for i in range(len(bits)):
        aList.append(16**(n-1))
        bList.append(16**(f-1))
        n-=1
        f-=1
        if i<len(bits):
            k=int(aList[i])
            
            if bits[i] in binadicth:
                j=bits[i]
                c=int(binadicth.get(j))
                valor+=k*c
                    
            else:
                c=int(bits[i])
                valor+=k*c
            
        if y<len(bits2):
            l=int(bList[y])
            if bits2[y] in binadicth:
                p=bits2[y]
                t=int(binadicth.get(p))
                valor2+=l*t
            
            else:
                t=int(bits2[y])
                valor2+=l*t
        y+=1 
    if(op==1):
        resultado=valor+valor2
        
    if(op==2):
        resultado=valor-valor2
        
    if(op==3):
        resultado=valor*valor2
        
    if(op==4):
        resultado=valor//valor2
      
    while resultado // 16 != 0:
            xList.append(str(resultado % 16))
            resultado = resultado // 16
            
    for v in range(len(xList)):
        if xList[v] in binadicths:
            
            conversion=str(binadicths.get(xList[v]))+conversion
        else:
            conversion=xList[v]+conversion
    
    return str(resultado)+ conversion

    
bits=raw_input('Dame un número hexadecimal: ')
bits2=raw_input('Dame un número hexadecimal: ')
op=int(input('Dame un número op 1 para +, 2 para -, 3 para *, 4 para /: '))
print 'Su valor decimal es',(Operaciones_Hexadecimal(bits,bits2,op))
