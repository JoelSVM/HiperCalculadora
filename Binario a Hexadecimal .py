# -*- coding: cp1252 -*-
numero = raw_input("Ingrese un número binario: ")
binadicth = {"0000" : "0","0001" : "1","0010" : "2","0011" : "3","0100" : "4","0101" : "5","0110" : "6","0111" : "7", "1000" : "8","1001" : "9","1010" : "a","1011" : "b","1100" : "c","1101" : "d","1110" : "e","1111" : "f"}
bin1 = ""
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
        print"R",binadicth.get(bin1)

    else:    
        bin1 = numero [B:Z]
        print"R ",binadicth.get(bin1)
    Z-=4
    cont-=4
