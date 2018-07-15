# -*- coding: cp1252 -*-
numero = raw_input("Ingrese un número binario: ")
binadict = {"000" : "0","001" : "1","010" : "2","011" : "3","100" : "4","101" : "5","110" : "6","111" : "7"}
bin1 = ""
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
        print"R ",binadict.get(bin1)

    else:    
        bin1 = numero [B:Z]
        print"R ",binadict.get(bin1)
    Z-=3
    cont-=3
        
     
   

