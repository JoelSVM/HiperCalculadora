#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def Decimal_Todos(decimal,base):
    binadicth = {"10" : "A","11" : "B","12" : "C","13" : "D","14" : "E","15" : "F"}
    aList=[]
    conversion = ""
    if base==16:
        while decimal // base != 0:
            aList.append(str(decimal % base))
            decimal = decimal // base
            
        for i in range(len(aList)):
            if aList[i] in binadicth:
                conversion=str(binadicth.get(aList[i]))+conversion
            else:
                conversion=aList[i]+conversion
                    
    else:
        while decimal // base != 0:
            conversion = str(decimal % base) + conversion
            decimal = decimal // base
    return str(decimal) + conversion

def Binario_Decimal(numeros):
    suma=0
    cont=0
    n=1
    t=len(numeros)
    j=t
    while cont!=t:
        j-=1
        if numeros[j]=="1":
            suma=suma+n
        cont+=1
        n=n*2
    return str(suma)

def Binario_Octal(numero):
    binadict = {"000" : "0","001" : "1","010" : "2","011" : "3","100" : "4","101" : "5","110" : "6","111" : "7"}
    bin1 = ""
    resultado=""
    cont=len(numero)
    B = len(numero)
    Z = len(numero)
    j=[1,2]
    while cont!=0 and cont!=-1 and cont!=-2:
        B = B-3
        if B==-1 or B==-2:
            B=0
            bin1 = numero [B:Z]
            while len(bin1)<=len(j):
                bin1="0"+bin1
            resultado=binadict.get(bin1)+resultado

        else:    
            bin1 = numero [B:Z]
            resultado=binadict.get(bin1)+resultado
        Z-=3
        cont-=3
        
    return resultado

def Binario_Hexadecimal(numero):
    binadicth = {"0000" : "0","0001" : "1","0010" : "2","0011" : "3","0100" : "4","0101" : "5","0110" : "6","0111" : "7", "1000" : "8","1001" : "9","1010" : "A","1011" : "B","1100" : "C","1101" : "D","1110" : "E","1111" : "F"}
    bin1 = ""
    resultado=""
    cont=len(numero)
    B = len(numero)
    Z = len(numero)
    j=[1,2,3]
    while cont!=0 and cont!=-1 and cont!=-2 and cont!=-3:
        B = B-4
        if B==-1 or B==-2 or B==-3:
            B=0
            bin1 = numero [B:Z]
            while len(bin1)<=len(j):
                bin1="0"+bin1
                resultado=binadicth.get(bin1)+resultado

        else:    
            bin1 = numero [B:Z]
            resultado=binadicth.get(bin1)+resultado
        Z-=4
        cont-=4
        
    return resultado

def octal_decimal(bits):
    aList=[]
    n=len(bits)
    valor=0
    k=0
    c=0
    for i in range(len(bits)):
        aList.append(8**(n-1))
        n -=1
        k=int(aList[i])
        c=int(bits[i])
        valor+=k*c
    
    return str(valor)

def octal_binario(numero):
    valor=""
    k=0
    bina = ["000","001","010","011","100",
            "101","110","111"]

    for i in range(len(numero)):
        k=int(numero[i])
        valor+=bina[k]
    return valor
def octal_Hexadecimal(numero):
    binadict = {"0" : "000","1" : "001","2" : "010","3" : "011","4" : "100","5" : "101","6" : "110","7" : "111"}
    binadicth = {"0000" : "0","0001" : "1","0010" : "2","0011" : "3","0100" : "4","0101" : "5","0110" : "6","0111" : "7", "1000" : "8","1001" : "9","1010" : "A","1011" : "B","1100" : "C","1101" : "D","1110" : "E","1111" : "F"}
    valor=""
    hexa=""
    resu=""
    for i in range(len(numero)):
        k=numero[i]
        valor+=binadict.get(k)
    a=len(valor)
    z=len(valor)
    pase=1
    j=[1,2,3]

    while pase==1:
        if a==1or a==2 or a==3 or a==4 or z==0:
            z=0
            resu=str(valor[z:a])
            while len(resu)<=len(j):
                    resu="0"+resu

            hexa=binadicth.get(resu)+hexa
            pase=0
        else:
            z=z-4
            resu=str(valor[z:a])
            a=a-4
            hexa=binadicth.get(resu)+hexa
                
                
    return hexa

def Hexadecimal_decimal(bits):
    binadicth = {"A" : "10","B" : "11","C" : "12","D" : "13","E" : "14","F" : "15"}
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
    
    return str(valor)

def Hexadecimal_Octal(numero):
    binadict = {"000" : "0","001" : "1","010" : "2","011" : "3","100" : "4","101" : "5","110" : "6","111" : "7"}
    binadicth = {"0" : "0000" ,"1" : "0001","2" : "0010","3" : "0011","4" : "0100","5" : "0101","6" : "0110","7" : "0111", "8" : "1000","9" : "1001","A" : "1010","B" : "1011","C" : "1100","D" : "1101","E" : "1110","F" : "1111"}
    valor=""
    octa=""
    resu=""
    for i in range(len(numero)):
            k=numero[i]
            valor+=str(binadicth.get(k))
    a=len(valor)
    z=len(valor)
    pase=1
    j=[1,2]
    while pase==1:
        if a==1 or a==2 or a==3 or z==0:
            z=0
            resu=str(valor[z:a])
            while len(resu)<=len(j):
                     resu="0"+resu
            octa=str(binadict.get(resu))+octa
            pase=0  
        else:
            z=z-3
            resu=str(valor[z:a])
            a=a-3
            octa=str(binadict.get(resu))+octa
            
    return octa

def Hexadecimal_Binario(numero):
    binadict = {"0" : "0000","1" : "0001","2" : "0010","3" : "0011","4" : "0100","5" : "0101","6" : "0110","7" : "0111","8" : "1000","9" : "1001","A" : "1010","B" : "1011","C" : "1100","D" : "1101","E" : "1110","F" : "1111"}
    valor=""

    for i in range(len(numero)):
        k=numero[i]
        valor+=str(binadict.get(k))

    return valor

def Operaciones_Hexadecimal(bits,bist2,op):
    binadicth = {"A" : "10","B" : "11","C" : "12","D" : "13","E" : "14","F" : "15"}
    binadicths = {"10" : "A","11" : "B","12" : "C","13" : "D","14" : "E","15" : "F"}
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

def Operaciones_Binarias(numeros,numeros2,opcion):
    suma=0
    suma2=0
    cont=0
    n=1
    conversion=""
    pase="true"
    if len(numeros)>=len(numeros2):
        t=len(numeros)
    if len(numeros)<len(numeros2):
        t=len(numeros2)       
    j=len(numeros)
    while pase=="true":
        while len(numeros)<t or len(numeros2)<t:

            if len(numeros)<t:
                numeros="0"+numeros
                print numeros
                
            if len(numeros2)<t:
                numeros2="0"+numeros2
                
        while cont!=t:
            j-=1
            if numeros[j]=="1" :    
                suma=suma+n

            if numeros2[j]=="1":
                suma2=suma2+n
                
            cont+=1
            n=n*2
            
            if cont==t and opcion==1:
                pase="false"
                resultado=suma+suma2
                
            if cont==t and opcion==2:
                pase="false"
                resultado=suma-suma2
                
            if cont==t and opcion==3:
                pase="false"
                resultado=suma*suma2
                
            if cont==t and opcion==4:
                pase="false"
                resultado=suma//suma2
            
    while resultado // 2 != 0:
        conversion = str(resultado % 2) + conversion
        resultado = resultado // 2
            
    return str(resultado) + conversion

def Operaciones_Decimales(numero,numero2,op):
    resultado=0
    if(op==1):
        resultado=numero+numero2
        
    if(op==2):
        resultado=numero-numero2
        
    if(op==3):
        resultado=numero*numero2
        
    if(op==4):
        resultado=numero//numero2

    return str(resultado)

def vbina(numero,pase):
    pase=0
    for i in numero:
        if int(i)>1:
            pase=1
      
    return pase

def voctal(numero,pase):
    pase=0
    for i in numero:
        
        if int(i)>7:
            pase=1
      
    return pase

def vhexa(numero,pase):
    pase=0
    for i in numero:
        str(i)
        if i!="A" and i!="B" and i!="C" and i!="D" and i!="E" and i!="F" and i!="0" and i!="1" and i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8" and i!="9":
            pase=1
      
    return pase



           



entrada="1"
pase=1
def menu():

    os.system('cls') 
    print ("CONVERSIONES")
    print("")
    print ("\t1 - Decimal a todos")
    print("")
    print ("\t2 - Binario Decimal")
    print ("\t3 - Binario Octal")
    print ("\t4 - Binario Hexadecimal")
    print("")
    print ("\t5 - Octal Decimal")
    print ("\t6 - Octal Binario")
    print ("\t7 - Octal Hexadecimal")
    print("")
    print ("\t8 - Hexadecimal Decimal")
    print ("\t9 - Hexadecimal Octal")
    print ("\t10 - Hexadecimal Binario")
    print ("\t20 - salir")
    print("")
    print ("OPERACIONES")
    print("")
    print ("\t11 - Hexadecimales")
    print ("\t12 - Octales")
    print ("\t13 - Binarias")
    print ("\t14 - Decimales")
    print ("\t20 - salir")
    print("")
 

while entrada=="1":
    menu()
    opcionMenu = input("Inserta un numero valor >> ")
 
    if opcionMenu==1:
        print ("")
        numero = int(input("Ingrese los valores Decimales: "))
        base = int(input("Ingrese la base: "))
        print "el resutado es: "+ Decimal_Todos(numero,base)
        print("")
        entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
        print("")
        print("")
        
    elif opcionMenu==2:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Binarios: ")        
            if vbina(numero,pase)==0:
                print "El Resultado en Decimal es: "+ Binario_Decimal(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
                
            else:
                print("Ingrese un numero valido")  
        pase=1
        
    elif opcionMenu==3:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Binarios: ")        
            if vbina(numero,pase)==0:
                print "El resutado en Octal es: "+ Binario_Octal(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
                
            else:
                print("Ingrese un numero valido")  
        pase=1
        
    elif opcionMenu==4:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Binarios: ")        
            if vbina(numero,pase)==0:
                print "El resutado en Octal es: "+ Binario_Hexadecimal(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
                
            else:
                print("Ingrese un numero valido")  
        pase=1
        
    elif opcionMenu==5:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Octales: ")
            if voctal(numero,pase)==0:
                print "El resutado en Decimal es: "+ octal_decimal(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
                
            else:
                print("Ingrese un numero valido")  
        pase=1       
        
    elif opcionMenu==6:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Octales: ")
            if voctal(numero,pase)==0:
                print "El resutado en Binario es: "+ octal_binario(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
                
            else:
                print("Ingrese un numero valido")  
        pase=1       
        
    elif opcionMenu==7:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Octales: ")
            if voctal(numero,pase)==0:
                print "El resutado en Hexadecimal es: "+ octal_Hexadecimal(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
                
            else:
                print("Ingrese un numero valido")  
        pase=1       
        
        
    elif opcionMenu==8:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Hexadecimales: ")
            if vhexa(numero,pase)==0:
                print "El resultado en Decimal es "+ Hexadecimal_decimal(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
            else:
                print("Ingrese un numero valido")
        pase=1        
        
    elif opcionMenu==9:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Hexadecimales: ")
            if vhexa(numero,pase)==0:
                print "El resultado en Octal es "+ Hexadecimal_Octal(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
            else:
                print("Ingrese un numero valido")
        pase=1        
        
    elif opcionMenu==10:
        while pase==1:
            print ("")
            numero=raw_input("Ingrese los valores Hexadecimales: ")
            if vhexa(numero,pase)==0:
                print "El resultado en Octal es "+ Hexadecimal_Binario(numero)
                print("")
                entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
                break
                print("")
                print("")
            else:
                print("Ingrese un numero valido")
        pase=1         
        
    elif opcionMenu==11:
        print ("")
        bits=raw_input('Dame un numero hexadecimal: ')
        bits2=raw_input('Dame un numero hexadecimal: ')
        op=int(input('Dame un numero 1 para +, 2 para -, 3 para *, 4 para /: '))
        print 'El resultado es'+(Operaciones_Hexadecimal(bits,bits2,op))
        print("")
        entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
        print("")
        print("")
        
    elif opcionMenu==12:
        print ("")
        bits=raw_input('Dame un numero octal: ')
        bits2=raw_input('Dame un numero octal: ')
        op=int(input('Dame un numero 1 para +, 2 para -, 3 para *, 4 para /: '))
        print 'El resultado es'+(Operaciones_Octales(bits,bits2,op))
        print("")
        entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
        print("")
        print("")
        
    elif opcionMenu==13:
        print ("")
        bits=str(input("Dame un numero Binario: "))
        bits2= str(input("Dame un numero Binario :"))
        op=int(input('Dame un numero 1 para +, 2 para -, 3 para *, 4 para /: '))
        print "El Resultado es: "+ Operaciones_Binarias(bits,bits2,op)
        print("")
        entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
        print("")
        print("")
        
        
    elif opcionMenu==14:
        print ("")
        bits=int(input("Dame un numero Decimal: "))
        bits2= int(input("Dame un numero Decimal :"))
        op=int(input('Dame un numero 1 para +, 2 para -, 3 para *, 4 para /: '))
        print "El Resultado es: "+ Operaciones_Decimales(bits,bits2,op)
        print("")
        entrada=str(input("Desea hacer otra conversion o operacion 1 para si  o 2 para no: "))
        print("")
        print("")

        
    elif opcionMenu==20:
        break
    else:
        print ("")
        print("No has pulsado una opcion Incorrecta")
        entrada=str(input("Desea volver a intentarlo 1 para si  o 2 para no: "))
        print("")
        
print("")        
print("GRACIAS")
